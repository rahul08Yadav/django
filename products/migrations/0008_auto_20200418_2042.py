# Generated by Django 2.1 on 2020-04-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200418_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cuisines',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rest_address',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='timings_and_perks',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
