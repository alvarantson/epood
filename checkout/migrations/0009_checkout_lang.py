# Generated by Django 3.0.2 on 2021-03-27 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0004_auto_20210311_1842'),
        ('checkout', '0008_auto_20210311_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(blank=True, max_length=999)),
                ('first_name', models.CharField(blank=True, max_length=999)),
                ('last_name', models.CharField(blank=True, max_length=999)),
                ('email', models.CharField(blank=True, max_length=999)),
                ('aadress', models.CharField(blank=True, max_length=999)),
                ('discounts_to_email', models.CharField(blank=True, max_length=999)),
                ('terms_conditions', models.CharField(blank=True, max_length=999)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
    ]