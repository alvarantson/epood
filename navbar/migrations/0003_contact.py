# Generated by Django 3.0.2 on 2021-03-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0002_lang_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=999)),
            ],
        ),
    ]
