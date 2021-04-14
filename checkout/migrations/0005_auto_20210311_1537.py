# Generated by Django 3.0.2 on 2021-03-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_buy_history_buyer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='buy_history',
            name='receipt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Receipt'),
        ),
    ]