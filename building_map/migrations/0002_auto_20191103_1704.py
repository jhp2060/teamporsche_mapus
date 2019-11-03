# Generated by Django 2.2.6 on 2019-11-03 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191103_1704'),
        ('building_map', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['name'], 'verbose_name_plural': 'Buildings'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'ordering': ['number'], 'verbose_name_plural': 'Floors'},
        ),
        migrations.RemoveField(
            model_name='building',
            name='campus',
        ),
        migrations.AddField(
            model_name='building',
            name='university',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.University'),
        ),
    ]