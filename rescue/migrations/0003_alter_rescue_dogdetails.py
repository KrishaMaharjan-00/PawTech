# Generated by Django 4.0.3 on 2022-03-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0002_rescue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescue',
            name='dogdetails',
            field=models.CharField(max_length=500),
        ),
    ]
