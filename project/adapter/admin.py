from django.contrib import admin

from adapter.models import Appliance, Sensor


class ApplianceAdmin(admin.ModelAdmin):
    list_display = ['oid', 'name', 'pid', 'appliance_type']


class SensorAdmin(admin.ModelAdmin):
    list_display = ['oid', 'unit', 'element', 'pid']


admin.site.register(Appliance, ApplianceAdmin)
admin.site.register(Sensor, SensorAdmin)
