# Generated by Django 2.2.6 on 2019-11-04 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('building_map', '0008_auto_20191104_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
