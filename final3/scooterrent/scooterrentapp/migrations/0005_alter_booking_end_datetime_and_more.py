# Generated by Django 4.2.1 on 2023-05-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scooterrentapp', '0004_remove_scooter_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_datetime',
            field=models.DateTimeField(),
        ),
    ]
