# Generated by Django 3.2.7 on 2023-02-03 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oniokoze', '0003_alter_history_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fish', to='oniokoze.spot'),
        ),
    ]
