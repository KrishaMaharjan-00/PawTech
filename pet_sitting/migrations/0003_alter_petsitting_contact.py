# Generated by Django 4.0.3 on 2022-03-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_sitting', '0002_alter_petsitting_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsitting',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
