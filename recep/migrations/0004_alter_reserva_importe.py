# Generated by Django 5.0.1 on 2024-01-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recep', '0003_remove_reserva_estadoreserva_remove_reserva_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='importe',
            field=models.FloatField(max_length=200),
        ),
    ]