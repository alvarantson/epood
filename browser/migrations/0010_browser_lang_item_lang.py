# Generated by Django 3.0.2 on 2021-03-27 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0004_auto_20210311_1842'),
        ('browser', '0009_product_tracking_group_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_products', models.CharField(blank=True, max_length=999)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Browser_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=999)),
                ('product_name', models.CharField(blank=True, max_length=999)),
                ('product_code', models.CharField(blank=True, max_length=999)),
                ('brand_name', models.CharField(blank=True, max_length=999)),
                ('search', models.CharField(blank=True, max_length=999)),
                ('reset_filters', models.CharField(blank=True, max_length=999)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
    ]
