from django.contrib import admin


# Register your models here.
from application.models import SensorUsage, Settings


class SensorUsageAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'value', 'datetime']


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['setting', 'value', 'description']


admin.site.register(SensorUsage, SensorUsageAdmin)
admin.site.register(Settings, SettingsAdmin)
