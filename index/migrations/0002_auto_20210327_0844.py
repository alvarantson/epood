# Generated by Django 3.0.2 on 2021-03-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='most_popular',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='our_partners',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='slogan',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='sub_title2',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='title',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='title2',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AddField(
            model_name='index_lang',
            name='top_sales',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
