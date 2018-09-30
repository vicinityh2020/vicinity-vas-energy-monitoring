from django.db import models


class Appliance(models.Model):
    name = models.CharField(max_length=100, null=False)
    oid = models.UUIDField(unique=True)
    pid = models.CharField(max_length=50)
    appliance_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    oid = models.UUIDField(unique=True)
    unit = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    pid = models.CharField(max_length=50)
    monitors = models.CharField(max_length=1, choices=(("W", "water"), ("P", "power")))

    def __str__(self):
        return self.unit
