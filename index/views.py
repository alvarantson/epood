from django.shortcuts import render

from browser.models import Product_lang, Item_lang
from .models import Index_lang

from navbar.models import Lang, Contact
from navbar.views import init_lang
# Create your views here.
def index(request):
	request = init_lang(request)

	grid = 4*2

	most_popular = Product_lang.objects.all().order_by("-product__views")[:grid]
	sales = Product_lang.objects.filter(product__special_price__range=[0.01,1000000000000]).order_by("-product__views")[:grid]
	featured = Product_lang.objects.filter(product__front_page=True).order_by("-product__views")[:grid]

	return render(request, "index.html", {
		"most_popular": most_popular,
		"lang": Index_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'sales': sales,
		"featured": featured,
		'item_lang': Item_lang.objects.get(lang=Lang.objects.get(lang=request.session["lang"])),
		'contact':Contact.objects.first(),
		'title': "front page",
		'description': "Vire e-kaubamaja varuosadele ja tarvikutele!",
		'tags': ",".join(["auto","varuosad","auto varuosad","bmw","audi","skoda", "Fixus", "Emart Auto", "autokaubad", "matkakaubad", "tööriistad", "jalgrattad", "tarvikud", "kodukaubad", "aiakaubad","vaba aeg","õli","aknapesu vedelik", "Motoral"])
		})