# Generated by Django 3.0.2 on 2021-03-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_checkout_lang_disclaimer'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout_lang',
            name='cart_empty',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='checkout_lang',
            name='over_qty',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]