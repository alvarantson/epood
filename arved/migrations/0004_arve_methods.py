# Generated by Django 3.0.2 on 2021-05-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arved', '0003_auto_20210529_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='arve',
            name='methods',
            field=models.TextField(blank=True, verbose_name='maksemeetod, summa'),
        ),
    ]