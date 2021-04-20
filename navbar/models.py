from django.db import models

# Create your models here.
class Lang(models.Model):
	lang = models.CharField(max_length=999, unique=True)
	name = models.CharField(max_length=999, unique=True, blank=True)
	flag = models.FileField()

	def __str__(self):
		return self.lang

class Navbar_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
	index = models.CharField(max_length=999, blank=True)
	categories = models.CharField(max_length=999, blank=True)
	browse = models.CharField(max_length=999, blank=True)
	checkout = models.CharField(max_length=999, blank=True)
	empty_cart = models.CharField(max_length=999, blank=True)
	cart_is_empty = models.CharField(max_length=999, blank=True)
	

	def __str__(self):
		return self.lang.lang


class Contact(models.Model):
	logo = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)
	firm_name = models.CharField(max_length=999, blank=True)
	address = models.CharField(max_length=999, blank=True)
