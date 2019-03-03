from django.db import models
from adapter import models as adapter_models

class SensorUsage(models.Model):
    value = models.FloatField()
    sensor = models.ForeignKey(adapter_models.Sensor, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    @staticmethod
    def get_usage_by_day(day, monitors):
        return SensorUsage.objects.filter(datetime__day=day.day,
                                          datetime__month=day.month,
                                          datetime__year=day.year,
                                          sensor__monitors=monitors).order_by('datetime')

    @staticmethod
    def get_usage_by_month(day, monitors):
        return SensorUsage.objects.filter(datetime__month=day.month, datetime__year=day.year, sensor__monitors=monitors).order_by('datetime')

    def __str__(self):
        return self.sensor.element + ' ' + str(self.value) + "@" + self.datetime.isoformat()


class Settings(models.Model):
    setting = models.CharField(max_length=20, unique=True)
    value = models.CharField(max_length=50, null=True, unique=False)
    description = models.CharField(max_length=240, unique=False, null=True)

    @staticmethod
    def get_threshold_value(setting_name):
        return Settings.objects.get(setting=setting_name)
