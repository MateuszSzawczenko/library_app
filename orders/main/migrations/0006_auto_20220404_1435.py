# Generated by Django 3.1.4 on 2022-04-04 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220313_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField()),
                ('isbn_number', models.CharField(max_length=50)),
                ('pages_number', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('page_title_href', models.URLField(max_length=1000)),
                ('language_published', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='listofproducts',
        ),
        migrations.DeleteModel(
            name='ListOfProducts',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
