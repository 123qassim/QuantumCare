# Generated by Django 5.1.3 on 2024-12-07 21:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cure', '0004_remove_contact_created_at_alter_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
