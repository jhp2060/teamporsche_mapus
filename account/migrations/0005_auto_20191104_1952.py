# Generated by Django 2.2.6 on 2019-11-04 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191104_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, related_name='_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
