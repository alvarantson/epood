from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
import unicodedata

from .models import Product, Product_lang, Category, Browser_lang, Item_lang
from navbar.models import Lang, Contact
from .import_motoral_from_api import import_motoral, import_motoral_categories
from navbar.views import init_lang
from django.db.models import Q
# Create your views here.

# õüöä non ascii char fix
# https://www.javaer101.com/en/article/17189410.html
def remove_diacritics(value):
     return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')

def reset_product_filters(request):
	request.session["product_filters"] = {}
	request.session["product_filters"]["min_price"] = 0.00
	request.session["product_filters"]["max_price"] = 100000.00
	return request


def browser(request, main_cat = None, cat = None):
	request = init_lang(request)
	product_list = Product_lang.objects.filter(lang=Lang.objects.get(lang="et"))
	sub_categories = None
	SEO_tags = []


	try:
		request.session["product_filters"] = request.session["product_filters"]
	except:
		request = reset_product_filters(request)

	# FILTERING
	if request.session["product_filters"]:


		try: 
			if request.session["product_filters"]["product_name"] != "":
				product_list = product_list.filter(name__contains = remove_diacritics(request.session["product_filters"]["product_name"]))
		except:
			pass

		try: 
			if request.session["product_filters"]["product_code"] != "":
				product_list = product_list.filter(product__code__contains = remove_diacritics(request.session["product_filters"]["product_code"]))
		except:
			pass


		try: 
			if request.session["product_filters"]["brand_name"] != "":
				product_list = product_list.filter(product__brand_name__contains = remove_diacritics(request.session["product_filters"]["brand_name"]))
		except:
			pass
		
		try:
			if request.session["product_filters"]["discounts_boolean"]:
				product_list = product_list.filter(~Q(product__special_price_end_date=None))
				request.session["product_filters"]["discounts_boolean"] = True
		except:
			request.session["product_filters"]["discounts_boolean"] = False

	# FILTER FORM FILTERING
	if request.POST:

		if request.POST["product_name"] != "":
			print(request.POST["product_name"])
			request.session["product_filters"]["product_name"] = request.POST["product_name"]
			product_list = product_list.filter(name__contains = remove_diacritics(request.POST["product_name"]))
		else:
			request.session["product_filters"]["product_name"] = ""


		if request.POST["product_code"] != "":
			request.session["product_filters"]["product_code"] = request.POST["product_code"]
			product_list = product_list.filter(product__code__contains = remove_diacritics(request.POST["product_code"]))
		else:
			request.session["product_filters"]["product_code"] = ""

		if request.POST["brand_name"] != "":
			request.session["product_filters"]["brand_name"] = request.POST["brand_name"]
			product_list = product_list.filter(product__brand_name__contains = remove_diacritics(request.POST["brand_name"]))
		else:
			request.session["product_filters"]["brand_name"] = ""



		if request.POST["product_min_price"] != "" or request.POST["product_max_price"] != "":

			if request.POST["product_min_price"] != "":
				request.session["product_filters"]["min_price"] = float(request.POST["product_min_price"])

			if request.POST["product_max_price"] != "":
				request.session["product_filters"]["max_price"] = float(request.POST["product_max_price"])

		try:
			if request.POST["discounts_boolean"]:
				product_list = product_list.filter(~Q(product__special_price_end_date=None))
				request.session["product_filters"]["discounts_boolean"] = True
		except:
			request.session["product_filters"]["discounts_boolean"] = False


	if request.session["product_filters"]["min_price"] != 0.00 or request.session["product_filters"]["max_price"] != 1000000.00:
		product_list = product_list.filter(product__price__range=(
			request.session["product_filters"]["min_price"],
			request.session["product_filters"]["max_price"]
			))



	try:
		if cat != None or request.session["product_filters"]["category"] != "":
			request.session["product_filters"]["category"] = cat
			product_list = product_list.filter(
				lang = Lang.objects.get(lang=request.session["lang"]),
				product__tracking_group__contains = cat
				)
			sub_categories = Category.objects.filter(
				lang = Lang.objects.get(lang=request.session["lang"]),
				parent = False, 
				code__contains = main_cat
				)
			main_cat = Category.objects.get(
				lang = Lang.objects.get(lang=request.session["lang"]),
				parent = True,
				code__contains = main_cat.replace("-","")
				)
	except:
		request.session["product_filters"]["category"] = ""
		pass


	product_list = product_list.order_by("-product__views")
	paginator = Paginator(product_list, 24) # Show 24 contacts per page.

	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)

	return render(request, "browser.html", {
		'products': products,
		'main_cat': main_cat,
		'sub_categories': sub_categories,
		'lang': Browser_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'item_lang': Item_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'contact':Contact.objects.first(),
		'title': "tooted",
		'description': "Vire e-kaubamaja toodete otsing!",
		'tags': ",".join(["auto","varuosad","auto varuosad","bmw","audi","skoda", "Fixus", "Emart Auto", "autokaubad", "matkakaubad", "tööriistad", "jalgrattad", "tarvikud", "kodukaubad", "aiakaubad","vaba aeg","õli","aknapesu vedelik", "Motoral"])
		})


def reset_filters(request):
	request = reset_product_filters(request)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def browser_import(request):
	duplicates = []
	imported_recap = (0,0,0)
	if request.POST:

		if "import-products" in request.POST["submit-btn"]:

			try:
				if request.POST["delete-all"]:
					Product.objects.all().delete()
			except:
				pass

			imported_recap = import_motoral() # return (added, updated, failed_to_add)

		if "import-categories" in request.POST["submit-btn"]:

			try:
				if request.POST["delete-all"]:
					Category.objects.all().delete()
			except:
				pass

			import_motoral_categories("et")

		if "find-duplicates" in request.POST["submit-btn"]:

			print("Started finding duplicates:")
			for item in Product.objects.all():
				if len(Product.objects.filter(code=item.code, price=item.price)) != 1:
					print(Product.objects.filter(code=item.code, price=item.price)[1])
					duplicates.append(Product.objects.filter(code=item.code, price=item.price)[1])

		if "remove-duplicates" in request.POST["submit-btn"]:

			for item in Product.objects.all():
				if len(Product.objects.filter(code=item.code, price=item.price)) != 1:
					Product.objects.filter(code=item.code, price=item.price)[1:].delete()


	return render(request, "browser_import.html", {
		"amount_of_products": len(Product.objects.all()),
		"amount_of_categories": len(Category.objects.all()),
		"duplicates":duplicates,
		"imported_recap": imported_recap,
		'contact':Contact.objects.first()
		})


def product(request, code = None):
	request = init_lang(request)
	product = Product_lang.objects.get(product__code = code)
	product.product.views += 1
	product.product.save()

	similar_products = Product_lang.objects.filter(product__tracking_group__contains=product.product.tracking_group).exclude(id=product.id)
	similar_products = similar_products.order_by("-product__views")[:4]

	return render(request, "product.html", {
		'product': product,
		"similar_products": similar_products,
		'lang': Item_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'item_lang': Item_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'contact':Contact.objects.first(),
		'title': product.name,
		'description': product.description,
		'tags': ",".join([product.name.replace(" ",",")]+["auto","varuosad","auto varuosad","bmw","audi","skoda", "Fixus", "Emart Auto", "autokaubad", "matkakaubad", "tööriistad", "jalgrattad", "tarvikud", "kodukaubad", "aiakaubad","vaba aeg","õli","aknapesu vedelik", "Motoral"])
		})


def categories(request):
	request = init_lang(request)

	cats = []
	for category in Category.objects.filter(lang=Lang.objects.get(lang="et"), parent=True):
		cats.append({
			"name": category.name,
			"code": category.code,
			"sub_categories": Category.objects.filter(code__contains=category.code+"-")
			})


	return render(request, "categories.html", {
		"categories": cats
		})

def categories_filter(request,main_cat, cat):
	if "-" not in main_cat:
		main_cat += "-"
	return browser(request,main_cat, cat)