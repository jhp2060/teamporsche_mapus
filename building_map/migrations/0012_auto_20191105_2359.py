# Generated by Django 2.2.6 on 2019-11-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_map', '0011_auto_20191105_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_type',
            field=models.CharField(choices=[('PRINTER', 'PRINTER'), ('CONSENT', 'CONSENT'), ('TOILET', 'TOILET'), ('LOCKER', 'LOCKER'), ('ATM', 'ATM'), ('TABLE', 'TABLE')], default=None, max_length=20),
        ),
    ]
