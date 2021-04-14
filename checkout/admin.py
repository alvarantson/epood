from django.contrib import admin
from .models import Buy_history, Stripe_key, Receipt_template, Checkout_lang
# Register your models here.
admin.site.register(Buy_history)
admin.site.register(Stripe_key)
admin.site.register(Receipt_template)
admin.site.register(Checkout_lang)