# Generated by Django 3.0.6 on 2020-05-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.BooleanField(default=False),
        ),
    ]