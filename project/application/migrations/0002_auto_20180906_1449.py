# Generated by Django 2.1 on 2018-09-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='threshold_power',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='threshold_water',
        ),
        migrations.AddField(
            model_name='settings',
            name='description',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='setting',
            field=models.CharField(default='DEFAULT', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='value',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
