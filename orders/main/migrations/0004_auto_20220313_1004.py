# Generated by Django 3.1.4 on 2022-03-13 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220313_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='amount_in_stock',
            new_name='amount',
        ),
    ]
