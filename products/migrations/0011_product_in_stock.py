# Generated by Django 3.2.5 on 2021-07-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210731_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
