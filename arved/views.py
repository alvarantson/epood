from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Arve, Arve_template
from navbar.models import Contact, Lang
# Create your views here.

def generate_invoice(db):
	contact = Contact.objects.first()
	template = Arve_template.objects.first().arve
	for key in [i for i in db if i not in ['csrfmiddlewaretoken','submit-btn', 'METHODS', 'CONTENT']]:
		template = template.replace("%"+key+"%", db[key])

	# PAYMENT METHODS

	final1 = template.split('%%PAYMENT_METHODS%%')
	template = final1[1].split('%%/PAYMENT_METHODS%%')[0]
	final1 = [final1[0],final1[1].split('%%/PAYMENT_METHODS%%')[1]]

	final = final1[0]
	items = [
	{
		'method':i.split(',')[0].strip(),
		'percentage':i.split(',')[1].strip()
		} for i in db['METHODS'].split('\n')
	]
	for item in items:
		temp = template
		temp = temp.replace('%PAYMENT_METHOD%',item['method'])
		temp = temp.replace('%PERCENTAGE%',item['percentage'])
		final += temp

	final += final1[1] 
	template = final

	# ITEMS

	final1 = template.split('%%ITEMS%%')
	template = final1[1].split('%%/ITEMS%%')[0]
	final1 = [final1[0],final1[1].split('%%/ITEMS%%')[1]]

	final = final1[0]
	items = [
	{
		'ITEM_NAME':i.split(',')[0].strip(),
		'ITEM_DISCOUNT':i.split(',')[1].strip(),
		'ITEM_PRICE':i.split(',')[2].strip(),
		'ITEM_QTY':i.split(',')[3].strip(),
		'ITEM_PRICE_TOTAL':i.split(',')[4].strip()
		} for i in db['CONTENT'].split('\n')
	]

	for item in items:
		temp = template
		for key in item:
			print(key, item[key])
			temp = temp.replace("%"+key+"%", item[key])
		final += temp

	final += final1[1] 
	template = final



	template = template.replace('%TITLE%',contact.title)
	template = template.replace('%LOGO_URL%',contact.logo.url)
	return template

def arved(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect("/")

	if request.POST:
		if 'generate-invoice' in request.POST['submit-btn']:
			return HttpResponse(generate_invoice(request.POST))

	return render(request, "arved.html", {})