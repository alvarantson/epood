from django.db import models

# Create your models here.
class Arve(models.Model):
	client = models.CharField(max_length=999, blank=True)
	client_address = models.CharField(max_length=999, blank=True)

	filler = models.CharField(max_length=999, blank=True)
	filler_address = models.CharField(max_length=999, blank=True)

	order = models.CharField(max_length=999, blank=True)
	order_id = models.CharField(max_length=999, blank=True)
	order_date = models.DateField(blank=True)

	date = models.DateField(auto_now=True, blank=True, null=True)
	deadline = models.DateField(blank=True, null=True)
	deadline_length = models.DateField(blank=True, null=True)

	methods = models.TextField("maksemeetod, summa", blank=True)
	content = models.TextField("asi, Al.%, Hind, Kogus, Reasumma", blank=True)

	VAT = models.FloatField(null=True, blank=True)
	total_without_VAT = models.FloatField(null=True, blank=True)
	rounding = models.FloatField(null=True, blank=True)
	total = models.FloatField(null=True, blank=True)

	def __str__(self):
		return str(self.id) + ": " + self.client + " - " + self.filler


class Arve_template(models.Model):
	arve = models.TextField(blank=True)