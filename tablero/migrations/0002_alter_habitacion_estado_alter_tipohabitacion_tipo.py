# Generated by Django 5.0.1 on 2024-01-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='estado',
            field=models.CharField(choices=[('D', 'Disponible'), ('O', 'Ocupado'), ('M', 'Mantenimiento'), ('R', 'Reservada')], default='Disponible', max_length=50),
        ),
        migrations.AlterField(
            model_name='tipohabitacion',
            name='tipo',
            field=models.CharField(choices=[('Doble Individual', 'Doble Individual'), ('Triple Individual', 'Triple Individual'), ('Matrimonial + Individual', 'Matrimonial + Individual'), ('Doble Matrimonial', 'Doble Matrimonial'), ('Matrimonial Queen', 'Matrimonial Queen'), ('Matrimonial King', 'Matrimonial King'), ('Matrimonial', 'Matrimonial')], default='Disponible', max_length=50),
        ),
    ]
