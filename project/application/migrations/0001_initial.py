# Generated by Django 2.1 on 2018-09-06 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adapter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adapter.Sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold_power', models.IntegerField()),
                ('threshold_water', models.IntegerField()),
            ],
        ),
    ]
