# Generated by Django 2.2.6 on 2019-11-03 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191103_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ['name'], 'verbose_name_plural': 'Universities'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name_plural': 'Users'},
        ),
    ]
