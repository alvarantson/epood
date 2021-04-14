from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseRedirect
from .models import Buy_history, Stripe_key, Receipt_template, Checkout_lang
import stripe
from browser.models import Product, Product_lang, Category
from navbar.models import Contact, Lang
from datetime import date

# Create your views here.
def generate_receipt(request):
	contact = Contact.objects.all()[0]

	template = Receipt_template.objects.all()[0].receipt
	template = template.replace('%TITLE%',contact.title)
	template = template.replace('%LOGO_URL%',contact.logo.url)
	template = template.replace('%ORDER_ID%',str(request.session['Buy_history']['buy_id']))
	template = template.replace('%DATE%',request.session['Buy_history']['date'])
	template = template.replace('%SELLER_NAME%',contact.firm_name)
	template = template.replace('%SELLER_ADDRESS%',contact.address)
	template = template.replace('%BUYER_NAME%',request.session['Buy_history']['buyer_first_name'] + " " + request.session['Buy_history']['buyer_last_name'])
	template = template.replace('%BUYER_PHONE%',request.session['Buy_history']['buyer_address'])
	template = template.replace('%BUYER_EMAIL%',request.session['Buy_history']['buyer_email'])
	template = template.replace('%TOTAL_PRICE%',str(round(request.session['Buy_history']['cart_total'],2))+"€")

	# PAYMENT METHODS

	final1 = template.split('%%PAYMENT_METHODS%%')
	template = final1[1].split('%%/PAYMENT_METHODS%%')[0]
	final1 = [final1[0],final1[1].split('%%/PAYMENT_METHODS%%')[1]]

	final = final1[0]
	items = [{'method':'card','percentage':'100%'}] # TODO
	for item in items:
		temp = template
		temp = temp.replace('%PAYMENT_METHOD%',item['method'] + " - " + item['percentage'])
		final += temp

	final += final1[1] 

	# BOUGHT ITEMS

	final1 = final.split('%%ITEMS%%')
	template = final1[1].split('%%/ITEMS%%')[0]
	final1 = [final1[0],final1[1].split('%%/ITEMS%%')[1]]

	final = final1[0]
	items = request.session['Buy_history']['cart']
	for item in items:
		print(item)
		temp = template
		temp = temp.replace('%ITEM_NAME%',item['name'])
		temp = temp.replace('%ITEM_QTY%',str(item['qty']))
		temp = temp.replace('%ITEM_PRICE%',str(round(item['price']*item['qty'],2))+"€")
		final += temp

	final += final1[1] 

	return final


def init_cart(request):
	try:
		request.session["cart"] = request.session["cart"]
	except:
		request.session["cart"] = []

	try:
		request.session["cart_total"] = request.session["cart_total"]
	except:
		request.session["cart_total"] = 0

	return request


def checkout(request):

	if not "cart" in request.session or request.session["cart"] == None:
		request.session["cart"] = []
		request.session["cart_total"] = 0

	qty_error = []

	# checkup on stock qty
	for i in range(len(request.session["cart"])):
		request.session["cart"][i]['stock'] =Product.objects.get(code=request.session["cart"][i]['code']).stock

		if request.session["cart"][i]['qty'] > Product.objects.get(code=request.session["cart"][i]['code']).stock:
			qty_error.append(request.session["cart"][i]['code'])

		if Product.objects.get(code=request.session["cart"][i]['code']).special_price and Product.objects.get(code=request.session["cart"][i]['code']).special_price_end_date:
			 if Product.objects.get(code=request.session["cart"][i]['code']).special_price_end_date > date.today():
			 	request.session["cart"][i]["price"] = Product.objects.get(code=request.session["cart"][i]['code']).special_price

	return render(request, "checkout.html", {
		"items": request.session["cart"],
		'stripe_public_key': Stripe_key.objects.all()[0].public_key,
		'qty_error': qty_error,
		'lang': Checkout_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'contact':Contact.objects.first()
		})


def add(request, code, qty):
	request = init_cart(request)

	qty = int(qty)
	product = Product_lang.objects.get(product__code=code)

	# IF ITEM ALREADY IN CART
	passer = False
	for i in range(len(request.session["cart"])):
		if request.session["cart"][i]["code"] == code:
			passer = True
			request.session["cart"][i]["qty"] += qty
			break

	if not passer:
		item_price = product.product.price
		if product.product.special_price and product.product.special_price_end_date:
			 if product.product.special_price_end_date > date.today():
			 	special = True
			 	item_price = product.product.special_price

		request.session["cart"].append({
			"code": product.product.code,
			"name": product.name,
			"stock": product.product.stock,
			"price": round(float(item_price),2),
			"old_price": round(float(product.product.price),2),
			"qty": qty, 
			"image_url": product.product.image_url
			})
		special = False

	request.session["cart_total"] += round(float(item_price),2) * qty
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def qty(request, code, qty):
	
	qty = int(qty)
	for i in range(len(request.session["cart"])):
		if request.session["cart"][i]["code"] == code:
			old_qty = request.session["cart"][i]["qty"]
			request.session["cart"][i]["qty"] = qty
			break

	request.session["cart_total"] += round(float(request.session["cart"][i]["price"] * qty) - float(request.session["cart"][i]["price"] * old_qty),2) 
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove(request, code):

	for item in request.session["cart"]:
		if code == item["code"]:
			request.session["cart_total"] -= int(item["qty"])*float(item["price"])
			request.session["cart"].remove(item)
			break

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def charge(request): # https://testdriven.io/blog/django-stripe-tutorial/
	if request.method == 'POST':
		stripe_private_key = Stripe_key.objects.all()[0].private_key
		stripe.api_key = stripe_private_key

		description = (
			'vire.ee -' + 
			request.POST["buyer_first_name"] + " " + 
			request.POST["buyer_last_name"] + " - " + 
			request.POST["buyer_email"]
			)

		charge = stripe.Charge.create(
			amount=int(float(request.session["cart_total"])*100),
			currency='eur',
			description= description,
			source=request.POST['stripeToken']
		)
		shopping_cart = request.session["cart"]
		shopping_cart_total = request.session["cart_total"]

		Buy_history.objects.create(
			shopping_cart = shopping_cart,
			shopping_cart_total = request.session["cart_total"],
			buyer_first_name = request.POST["buyer_first_name"],
			buyer_last_name = request.POST["buyer_last_name"],
			buyer_email = request.POST["buyer_email"],
			buyer_address = request.POST["buyer_address"]
			)
		buy_history = Buy_history.objects.filter(shopping_cart = shopping_cart, buyer_email = request.POST["buyer_email"], buyer_address = request.POST["buyer_address"])[0]
		request.session["Buy_history"] = {
			"cart":shopping_cart,
			"cart_total":buy_history.shopping_cart_total,
			"buyer_first_name":buy_history.buyer_first_name,
			"buyer_last_name":buy_history.buyer_last_name,
			"buyer_email":buy_history.buyer_email,
			"buyer_address":buy_history.buyer_address,
			"buy_id":buy_history.id,
			"date":str(buy_history.date.strftime("%d %B, %Y"))
			}

		buy_history.receipt = generate_receipt(request)
		buy_history.save()

		try:
			if request.POST["mail_list"]:
				Mail_list.objects.create(email=request.POST["buyer_email"])
		except:
			pass

		# STOCK UPDATE
		for i in range(len(shopping_cart)):
			item = Product.objects.get(code=shopping_cart[i]['code'])
			item.stock -= shopping_cart[i]['qty']
			item.bought += shopping_cart[i]['qty']
			item.save()

		request.session["cart"] = []
		request.session["cart_total"] = 0
		request.session["cart_total_int"] = 0


		return render(request, 'charge.html', {
			"receipt":buy_history.receipt,
			'contact':Contact.objects.first()
			})


def empty(request):
	request.session["cart"] = []
	request.session["cart_total"] = 0

	return HttpResponseRedirect(request.META['HTTP_REFERER'])