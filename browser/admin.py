from django.contrib import admin
from .models import Product, Product_lang, Category, Browser_lang, Item_lang
# Register your models here.

class Product_admin(admin.ModelAdmin):
	search_fields = ['code']


admin.site.register(Product, Product_admin)
admin.site.register(Product_lang)
admin.site.register(Category)
admin.site.register(Browser_lang)
admin.site.register(Item_lang)