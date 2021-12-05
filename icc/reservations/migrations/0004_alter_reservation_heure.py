# Generated by Django 3.2.6 on 2021-12-04 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_heure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='heure',
            field=models.TimeField(blank=True, choices=[(datetime.time(8, 0), '08:00'), (datetime.time(8, 30), '08:30'), (datetime.time(9, 0), '09:00'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 0), '10:00'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 0), '11:00'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 0), '12:00'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 30), '17:30')], null=True, verbose_name='Heure: HH:MM (H+1)'),
        ),
    ]
