# Generated by Django 3.1.4 on 2022-04-04 13:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220404_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofbooks',
            old_name='author',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='isbn_number',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='language_published',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='page_title_href',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='pages_number',
        ),
        migrations.RemoveField(
            model_name='listofbooks',
            name='title',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField()),
                ('isbn_number', models.CharField(max_length=50)),
                ('pages_number', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('page_title_href', models.URLField(max_length=1000)),
                ('language_published', models.CharField(max_length=100)),
                ('listofbooks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listofbooks')),
            ],
        ),
    ]
