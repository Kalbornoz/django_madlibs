# Generated by Django 4.1.2 on 2022-10-26 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madlibs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillIns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
                ('field3', models.CharField(max_length=100)),
                ('field4', models.CharField(max_length=100)),
                ('field5', models.CharField(max_length=100)),
                ('field6', models.CharField(max_length=100)),
                ('field7', models.CharField(max_length=100)),
            ],
        ),
    ]
