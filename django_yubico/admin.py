from django.contrib import admin

from django_yubico.models import YubicoKey


class YubicoKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_id', 'client_id', 'secret_key', 'enabled')
    search_fields = ['user', 'device_id', 'client_id']

admin.site.register(YubicoKey, YubicoKeyAdmin)
