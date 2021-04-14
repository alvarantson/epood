# Generated by Django 3.0.6 on 2020-05-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
        ('browser', '0003_auto_20200511_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=999, null=True)),
                ('name', models.CharField(blank=True, max_length=999, null=True)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navbar.Lang')),
            ],
        ),
    ]
