# Generated by Django 4.2.1 on 2023-05-24 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scooterrentapp', '0003_booking_end_datetime_booking_start_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scooter',
            name='booked',
        ),
    ]
