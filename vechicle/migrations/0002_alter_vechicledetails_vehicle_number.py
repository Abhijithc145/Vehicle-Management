# Generated by Django 4.1 on 2022-08-26 07:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vechicledetails',
            name='vehicle_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
