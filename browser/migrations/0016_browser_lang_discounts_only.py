# Generated by Django 3.0.2 on 2021-04-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0015_auto_20210416_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='browser_lang',
            name='discounts_only',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]