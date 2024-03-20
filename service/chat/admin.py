from django.contrib import admin

from chat.models import Group, Event, Message


@admin.register(Group)
@admin.register(Event)
@admin.register(Message)
