# Generated by Django 3.2.12 on 2024-04-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp', '0002_rename_order_items_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_updated',
            field=models.DateField(),
        ),
    ]
