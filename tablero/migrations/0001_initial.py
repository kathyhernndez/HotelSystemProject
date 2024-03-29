# Generated by Django 5.0.1 on 2024-01-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(unique=True)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado'), ('Mantenimiento', 'Mantenimiento'), ('Reservada', 'Reservada')], default='Disponible', max_length=50)),
                ('precio', models.FloatField(max_length=10)),
                ('tipo', models.CharField(choices=[('Doble Individual', 'Doble Individual'), ('Triple Individual', 'Triple Individual'), ('Matrimonial + Individual', 'Matrimonial + Individual'), ('Doble Matrimonial', 'Doble Matrimonial'), ('Matrimonial Queen', 'Matrimonial Queen'), ('Matrimonial King', 'Matrimonial King'), ('Matrimonial', 'Matrimonial')], default='Doble Individual', max_length=50)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'db_table': 'Habitacion',
            },
        ),
    ]
