# Generated by Django 3.0.2 on 2020-02-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200201_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='destination',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='plate_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
