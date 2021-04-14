from django.shortcuts import render
from django.http import HttpResponseRedirect

from checkout.views import init_cart
from .models import Lang
from browser.models import Category

# Create your views here.
def init_lang(request):

	request = init_cart(request)

	try:
		request.session["lang"] = request.session["lang"]
	except:
		request.session["lang"] = "et"


	try:
		request.session["lang_select"] = request.session["lang_select"]
	except:
		request.session["lang_select"] = []
		for lang in Lang.objects.all():
			request.session["lang_select"].append({
				"lang": lang.lang,
				"name": lang.name,
				"img_url": lang.flag.url
				})


			
	try:
		request.session["nav_cats"] = request.session["nav_cats"]
	except:
		request.session["nav_cats"] = []
		for nav_cat in Category.objects.filter(parent=True, lang = Lang.objects.get(lang=request.session["lang"])):
			request.session["nav_cats"].append({
				"name": nav_cat.name,
				"code": nav_cat.code
				})


	return request


def change_lang(request, lang):
	request.session["lang"] = "et"
	return HttpResponseRedirect(request.META['HTTP_REFERER'])