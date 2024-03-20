from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from django.urls import reverse


USER = get_user_model()


class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=32)
    members = models.ManyToManyField(USER, related_name="groups")

    class Meta:
        verbose_name = "Группу"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"Чат {self.name} - {self.uuid}"

    def get_absolute_url(self):
        return reverse("group", args=[str(self.uuid)])

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = datetime.strftime("%d.%m.%Y %H:%M:%S")

        super().save(*args, **kwargs)

    def add_user(self, user):
        self.members.add(user)
        self.events.create(type="Join", user=user)
        self.save()

    def remove_user(self, user):
        self.members.remove(user)
        self.events.create(type="Leave", user=user)
        self.save()
    


class Event(models.Model):
    CHOICES = [
        ("Join", "присоединился"),
        ("Leave", "покинул"),
    ]
    type = models.CharField(max_length=16, choices=CHOICES)
    description = models.CharField(
        max_length=128, help_text="Краткое описание", editable=False
    )
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="events")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def save(self, *args, **kwargs):
        self.description = f"{self.user} {self.type} в {self.group.name} группу"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.description}"
    


class Message(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="messages")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
