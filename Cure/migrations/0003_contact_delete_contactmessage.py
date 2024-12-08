# Generated by Django 5.1.3 on 2024-12-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cure', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactMessage',
        ),
    ]