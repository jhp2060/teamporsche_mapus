# Generated by Django 2.2.6 on 2019-10-30 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.University')),
            ],
        ),
    ]