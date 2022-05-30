# Generated by Django 4.0.4 on 2022-05-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('predict', '0002_delete_disease'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=500)),
                ('preventions', models.CharField(max_length=500)),
                ('primarymedication', models.CharField(max_length=500)),
            ],
        ),
    ]