# Generated by Django 2.2.4 on 2019-09-04 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CorrectionApp', '0007_auto_20190903_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_end_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 13, 28, 14, 466790)),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booking_start_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 13, 28, 14, 466790)),
        ),
    ]
