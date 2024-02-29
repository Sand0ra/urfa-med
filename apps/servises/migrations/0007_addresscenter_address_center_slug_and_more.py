# Generated by Django 4.2 on 2024-02-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servises', '0006_addresscenter_description_ky_addresscenter_title_ky_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresscenter',
            name='address_center_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='analysis',
            name='analysis_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='analysiscategory',
            name='analysis_category_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='diagnostic_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='diagnosticcategory',
            name='diagnostic_category_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='diagnosticsubcategory',
            name='diagnostic_subcategory_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='polyclinic',
            name='polyclinic_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='polycliniccategory',
            name='polyclinic_category_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='region',
            name='region_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='rehabilitation_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='rehabilitationcategory',
            name='rehabilitation_category_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
