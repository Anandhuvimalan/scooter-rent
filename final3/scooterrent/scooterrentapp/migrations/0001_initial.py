# Generated by Django 4.2.1 on 2023-05-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='scooters/')),
                ('kilometer_range', models.IntegerField()),
                ('price', models.IntegerField()),
                ('booked', models.BooleanField(default=False)),
            ],
        ),
    ]
