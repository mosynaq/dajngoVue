# Generated by Django 3.1.1 on 2020-09-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_workofart_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='workofart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Price'),
        ),
    ]
