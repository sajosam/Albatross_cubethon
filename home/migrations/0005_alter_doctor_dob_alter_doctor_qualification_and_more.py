# Generated by Django 4.0.4 on 2022-05-27 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_doctor_is_active_alter_doctor_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 11, 12, 40, 203273)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date_of_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 11, 12, 40, 201277)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]