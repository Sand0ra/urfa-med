# Generated by Django 4.2 on 2024-02-25 11:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servises', '0005_remove_addresscenter_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresscenter',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='addresscenter',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='Patient_instructions_ky',
            field=models.TextField(null=True, verbose_name='Инструкции для пациента'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='analysis_description_ky',
            field=models.TextField(null=True, verbose_name='Описание анализа'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='analysis_name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название анализа'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='expected_results_ky',
            field=models.TextField(null=True, verbose_name='Ожидаемые результаты'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='procedure_description_ky',
            field=models.TextField(null=True, verbose_name='Описание процедуры'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='results_delivery_time_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Время доставки результатов'),
        ),
        migrations.AddField(
            model_name='analysiscategory',
            name='category_description_ky',
            field=models.TextField(null=True, verbose_name='Описание Категория'),
        ),
        migrations.AddField(
            model_name='analysiscategory',
            name='category_name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Категорий анализа'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='diagnostic_name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название диагностики'),
        ),
        migrations.AddField(
            model_name='diagnosticcategory',
            name='diagnostic_category_name_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название категории диагностики'),
        ),
        migrations.AddField(
            model_name='diagnosticsubcategory',
            name='diagnostic_subcategory_description_ky',
            field=models.TextField(null=True, verbose_name='Описание подкатегории диагностики'),
        ),
        migrations.AddField(
            model_name='diagnosticsubcategory',
            name='diagnostic_subcategory_name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название подкатегории диагностики'),
        ),
        migrations.AddField(
            model_name='polyclinic',
            name='about_procedure_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание процедур'),
        ),
        migrations.AddField(
            model_name='polyclinic',
            name='about_service_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание услуг'),
        ),
        migrations.AddField(
            model_name='polyclinic',
            name='polyclinic_name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название поликлиники'),
        ),
        migrations.AddField(
            model_name='polycliniccategory',
            name='polyclinic_category_name_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название категории поликлиники'),
        ),
        migrations.AddField(
            model_name='region',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='название региона'),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='rehabilitation_description_ky',
            field=models.TextField(null=True, verbose_name='Описание реабилитации'),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='rehabilitation_name_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Название реабилитации'),
        ),
        migrations.AddField(
            model_name='rehabilitationcategory',
            name='rehabilitation_category_name_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Категорий реабилитации'),
        ),
    ]
