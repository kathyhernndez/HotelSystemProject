# Generated by Django 5.0.1 on 2024-01-31 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recep', '0004_alter_cliente_apellido_alter_cliente_cedula_and_more'),
        ('tablero', '0006_alter_habitacion_estado_alter_habitacion_moneda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recep.cliente', verbose_name='Selecciona el cliente. Si el cliente no encuentra registrado, haz click en registrar cliente, para registrar uno nuevo.'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablero.habitacion', verbose_name='Selecciona la habitacion'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='importe',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Importe de Pago de la Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='metodoPago',
            field=models.CharField(choices=[('Divisas', 'Divisas'), ('Pago Movil', 'Pago Movil'), ('Transferencia', 'Transferencia'), ('Binance', 'Binance'), ('Zinli', 'Zinli'), ('Paypal', 'Paypal'), ('Punto de Venta', 'Punto de Venta'), ('Tarjeta de Credito', 'Tarjeta de Credito'), ('Biopago', 'Biopago')], default='Divisas', verbose_name='Metodo de Pago Utilizado'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='moneda',
            field=models.CharField(choices=[('Dolares', 'Dolares'), ('Bolivares', 'Bolivares'), ('Pesos CO', 'Pesos CO'), ('USDT', 'USDT'), ('BTC', 'BTC')], default='Dolares', verbose_name='Moneda Utilizada para el pago de la Reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='tiempoEstadia',
            field=models.PositiveIntegerField(max_length=2, null=True, verbose_name='Dias de Estadia del Cliente'),
        ),
    ]
