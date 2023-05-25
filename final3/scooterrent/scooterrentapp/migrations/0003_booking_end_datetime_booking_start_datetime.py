# Generated by Django 4.2.1 on 2023-05-24 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scooterrentapp', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]