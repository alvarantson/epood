# Generated by Django 3.0.2 on 2021-03-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_receipt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_history',
            name='receipt',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
    ]