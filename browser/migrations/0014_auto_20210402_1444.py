# Generated by Django 3.0.2 on 2021-04-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0013_auto_20210402_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='special_price_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
