# Generated by Django 2.2.6 on 2019-11-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_map', '0003_auto_20191103_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='map_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
