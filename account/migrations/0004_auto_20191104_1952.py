# Generated by Django 2.2.6 on 2019-11-04 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191103_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(default=None, null=True, related_name='_user_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
