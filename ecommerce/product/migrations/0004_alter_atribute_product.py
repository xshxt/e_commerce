# Generated by Django 4.2 on 2023-05-29 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_atribute_products_remove_orderitem_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atribute',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atributes', to='product.producte'),
        ),
    ]
