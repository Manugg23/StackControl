# Generated by Django 4.2.7 on 2024-04-07 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_producto_usuario_proveedor_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='usuario',
        ),
    ]