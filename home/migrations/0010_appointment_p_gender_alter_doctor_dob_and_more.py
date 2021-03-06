# Generated by Django 4.0.4 on 2022-05-27 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_appointment_time_alter_doctor_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='p_gender',
            field=models.CharField(default='nil', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 22, 15, 28, 420632)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date_of_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 22, 15, 28, 419631)),
        ),
    ]
