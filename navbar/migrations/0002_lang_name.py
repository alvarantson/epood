# Generated by Django 3.0.6 on 2020-05-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lang',
            name='name',
            field=models.CharField(blank=True, max_length=999, unique=True),
        ),
    ]
