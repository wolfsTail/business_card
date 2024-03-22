from django.contrib import admin

from chat.models import Group, Event, Message


admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Message)
