from django.db import models
from navbar.models import Lang
# Create your models here.
class Browser_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)

	title = models.CharField(max_length=999, blank=True)

	product_name = models.CharField(max_length=999, blank=True)
	product_code = models.CharField(max_length=999, blank=True)
	brand_name = models.CharField(max_length=999, blank=True)
	sub_categories = models.CharField(max_length=999, blank=True)
	discounts_only = models.CharField(max_length=999, blank=True)

	search = models.CharField(max_length=999, blank=True)
	reset_filters = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.lang.lang

class Item_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)

	similar_products = models.CharField(max_length=999, blank=True)
	add_to_cart = models.CharField(max_length=999, blank=True)
	in_stock = models.CharField(max_length=999, blank=True)
	QTY = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.lang.lang


class Product(models.Model):
	code = models.CharField(max_length=999, null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	stock = models.IntegerField(null=True, blank=True)
	special_price = models.FloatField(null=True, blank=True)
	special_price_percentage = models.IntegerField(null=True, blank=True)
	special_price_end_date = models.DateField(null=True, blank=True, default=None)
	image_url = models.CharField(max_length=999, null=True, blank=True)
	tracking_group = models.CharField(max_length=999, null=True, blank=True)
	tracking_group_parent = models.CharField(max_length=999, null=True, blank=True)
	EAN = models.CharField(max_length=999, null=True, blank=True)
	brand_name = models.CharField(max_length=999, null=True, blank=True)
	brand_image_url = models.CharField(max_length=999, null=True, blank=True)
	measurements = models.CharField(max_length=999, null=True, blank=True)
	items_in_package = models.CharField(max_length=999, null=True, blank=True)
	weight = models.FloatField(null=True, blank=True)
	more_images = models.CharField(max_length=999, null=True, blank=True)
	front_page = models.BooleanField(default=False)

	views = models.IntegerField(default=0)
	bought = models.IntegerField(default=0)

	def __str__(self):
		return self.code


class Product_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	name = models.CharField(max_length=999, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	categories = models.CharField(max_length=9999, null=True, blank=True)

	def __str__(self):
		return self.product.code + " - " + self.lang.lang + " - " + self.name


class Category(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
	code = models.CharField(max_length=999, blank=True, null=True)
	name = models.CharField(max_length=999, blank=True, null=True)
	parent = models.BooleanField(default=False)

	def __str__(self):
		if not self.parent:
			return self.lang.lang + " - " + self.code + ": " + self.name
		else:
			return self.lang.lang + " PARENT - " + self.code + ": " + self.name