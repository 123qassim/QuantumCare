# Generated by Django 5.1.3 on 2024-12-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(choices=[('Pharmacy', 'Pharmacy'), ('Laboratory', 'Laboratory'), ('Dentistry', 'Dentistry'), ('Surgery', 'Surgery')], max_length=50)),
                ('preferred_date', models.DateField(blank=True, null=True)),
                ('preferred_time', models.TimeField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('insurance_provider', models.CharField(blank=True, max_length=100, null=True)),
                ('policy_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('appointment_date', models.DateField(auto_now_add=True)),
                ('appointment_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('start_date', models.DateField()),
                ('areas_of_interest', models.CharField(max_length=255)),
                ('intro_letter', models.FileField(upload_to='intro_letters/')),
            ],
        ),
    ]
