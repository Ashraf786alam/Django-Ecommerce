# Generated by Django 3.1.2 on 2020-12-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]