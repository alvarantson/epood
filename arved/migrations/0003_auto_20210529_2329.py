# Generated by Django 3.0.2 on 2021-05-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arved', '0002_arve_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='arve',
            name='VAT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arve',
            name='deadline_length',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arve',
            name='rounding',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arve',
            name='total_without_VAT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arve',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='arve',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arve',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]