# Generated by Django 4.2 on 2023-06-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biser', '0004_alter_jewelry_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Закончен ли заказ'),
        ),
    ]
