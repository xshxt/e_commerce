# Generated by Django 4.2 on 2023-06-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=True, verbose_name='Оплата'),
        ),
    ]
