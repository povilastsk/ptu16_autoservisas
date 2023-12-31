# Generated by Django 4.2.5 on 2023-09-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0002_car_plate_car_vin_alter_car_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'pending'), (1, 'processing'), (2, 'completed'), (3, 'cancelled')], default=0, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='partservice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
    ]
