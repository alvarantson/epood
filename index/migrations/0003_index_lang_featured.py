# Generated by Django 3.0.2 on 2021-03-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210327_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='featured',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]