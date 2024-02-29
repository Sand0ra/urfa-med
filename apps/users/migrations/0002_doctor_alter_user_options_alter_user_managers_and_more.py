# Generated by Django 4.2 on 2024-02-14 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/doctors/')),
                ('specialization', models.TextField(blank=True, default='Доктор практикант', null=True, verbose_name='Специализация')),
                ('upcoming_appointment', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Докторы',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Man', 'Мужской'), ('Women', 'Женский')], max_length=10, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='user',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='upcoming_appointment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Man', 'Мужской'), ('Women', 'Женский')], max_length=10, null=True, verbose_name='Пол')),
                ('upcoming_appointment', models.DateTimeField(blank=True, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пациента',
                'verbose_name_plural': 'Профили пациентов',
            },
        ),
    ]
