# Generated by Django 4.2 on 2023-06-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(max_length=300, verbose_name='Адрес клиента'),
        ),
    ]