# Generated by Django 3.2.7 on 2023-01-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oniokoze', '0005_auto_20230125_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='unit',
            field=models.TextField(blank=True, null=True, verbose_name='単位'),
        ),
    ]