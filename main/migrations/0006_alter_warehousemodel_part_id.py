# Generated by Django 4.1 on 2022-08-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_warehousemodel_part_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousemodel',
            name='part_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
