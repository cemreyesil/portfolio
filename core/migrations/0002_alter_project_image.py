# Generated by Django 4.2.2 on 2025-03-10 21:36

from django.db import migrations, models
import portfolio_cemre.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='', storage=portfolio_cemre.custom_storage.ImageSettingStorage(), upload_to='', verbose_name='Image'),
        ),
    ]
