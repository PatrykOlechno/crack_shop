# Generated by Django 2.2 on 2020-07-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
