from django.shortcuts import render
from django.http import HttpResponseRedirect
from browser.models import Product_lang, Product
from django.db.models import Q
from navbar.models import Lang, Contact
# Create your views here.
def haldus(request):
	if not request.user.is_superuser: return HttpResponseRedirect('/admin')
	return render(request, 'haldus.html', {})

def discount(request):
	if not request.user.is_superuser: return HttpResponseRedirect('/admin')

	if request.POST:
		if request.POST["submit-btn"] == "remove-all-discounts":
			for item in Product.objects.filter(~Q(special_price_end_date=None)):
				item.special_price = None
				item.special_price_percentage = None
				item.special_price_end_date = None
				item.save()


		if request.POST["submit-btn"] == "remove-discount":
			item = Product.objects.get(code=request.POST["code"])
			item.special_price = None
			item.special_price_percentage = None
			item.special_price_end_date = None
			item.save()


		if request.POST["submit-btn"] == "alter-all-discounts-date":
			for item in Product.objects.filter(~Q(special_price_end_date=None)):
				item.special_price_end_date = request.POST["discounts-new-date"].replace('.','-')
				item.save()


		if request.POST["submit-btn"] == "bulk-add-discounts":

			for code in request.POST["codes"].split('\n'):
				code = code.strip()
				if code == "":
					continue
					
				item = Product.objects.get(code=code)

				item.special_price_end_date = request.POST["discounts-new-date"].replace('.','-')
				item.special_price_percentage = int(request.POST["percentage"])
				item.special_price = round(item.price*(int(request.POST["percentage"])/100),2)
				item.save()

	return render(request, 'discount.html', {
		'sales': Product_lang.objects.filter(~Q(product__special_price_end_date=None)),
		'contact':Contact.objects.first()
		})

def salesstats(request):

	if not request.user.is_superuser: return HttpResponseRedirect('/admin')

	sold_items = []
	sold_items = Product_lang.objects.filter(product__bought__range=[1,1000000000000]).order_by("-product__bought")

	total_sales = 0 # items sold * prices
	total_sold = 0 # items sold

	for item in sold_items:
		total_sold += item.product.bought 
		total_sales += item.product.bought * item.product.price

	return render(request, 'salesstats.html', {
		'items': sold_items,
		'total_sales': total_sales,
		'total_sold': total_sold,
		'contact':Contact.objects.first()
		})
