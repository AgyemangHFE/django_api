# Generated by Django 3.2.12 on 2022-09-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangonative', '0011_alter_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order',
            field=models.JSONField(default=dict),
        ),
    ]