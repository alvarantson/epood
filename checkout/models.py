from django.db import models
from navbar.models import Lang
# Create your models here.
class Checkout_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)

	total = models.CharField(max_length=999, blank=True)

	first_name = models.CharField(max_length=999, blank=True)
	last_name = models.CharField(max_length=999, blank=True)
	email = models.CharField(max_length=999, blank=True)
	aadress = models.CharField(max_length=999, blank=True)

	disclaimer = models.TextField(blank=True)

	discounts_to_email = models.CharField(max_length=999, blank=True)
	terms_conditions = models.CharField(max_length=999, blank=True)

	cart_empty = models.CharField(max_length=999, blank=True)
	over_qty = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.lang.lang


class Receipt_template(models.Model):
	receipt = models.TextField(blank=True)


class Buy_history(models.Model):

	shopping_cart = models.TextField(blank=True)
	shopping_cart_total = models.FloatField(blank=True, default=0)
	date = models.DateField(auto_now_add=True)
	buyer_email = models.CharField(max_length=999, null=True, blank=True)
	buyer_first_name = models.CharField(max_length=999, null=True, blank=True)
	buyer_last_name = models.CharField(max_length=999, null=True, blank=True)
	buyer_address = models.CharField(max_length=999, blank=True)
	total = models.FloatField(null=True, blank=True)
	receipt = models.TextField()

	def __str__(self):
		return str(self.date) + " - €" + str(self.shopping_cart_total) + " - " + self.buyer_email

class Stripe_key(models.Model):
	test = models.CharField(max_length=999, blank=True, default="Test")
	public_key = models.CharField(max_length=999)
	private_key = models.CharField(max_length=999)

	def __str__(self):
		return self.test