from django.db import models

# Create your models here.
class Lang(models.Model):
	lang = models.CharField(max_length=999, unique=True)
	name = models.CharField(max_length=999, unique=True, blank=True)
	flag = models.FileField()

	def __str__(self):
		return self.lang

class Contact(models.Model):
	logo = models.ImageField(blank=True)
	title = models.CharField(max_length=999, blank=True)
	firm_name = models.CharField(max_length=999, blank=True)
	address = models.CharField(max_length=999, blank=True)
