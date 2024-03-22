from django.contrib import admin

from facilities.models import Plan, Service, Consumer


admin.site.register(Service)
admin.site.register(Consumer)
admin.site.register(Plan)