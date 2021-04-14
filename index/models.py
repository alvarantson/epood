from django.db import models
from navbar.models import Lang
# Create your models here.
class Index_lang(models.Model):
	lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
	title = models.CharField(max_length=999, blank=True)
	slogan = models.CharField(max_length=999, blank=True)

	featured = models.CharField(max_length=999, blank=True)
	most_popular = models.CharField(max_length=999, blank=True)
	title2 = models.CharField(max_length=999, blank=True)
	sub_title2 = models.CharField(max_length=999, blank=True)

	top_sales = models.CharField(max_length=999, blank=True)
	our_partners = models.CharField(max_length=999, blank=True)
	def __str__(self):
		return self.lang.lang