# Generated by Django 2.2.12 on 2022-10-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]
