from django.db import models

from users.models import CustomUser as User


class Service(models.Model):
    name = models.CharField(max_length=128, unique=True)
    brief = models.CharField(max_length=256)
    base_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    description = models.TextField()

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"Наименование: {self.name}"


class Plan(models.Model):
    PLAN_TYPES = [
        ("light", "Лайт"),
        ("base", "Базовый"),
        ("premium", "Премиум"),
        ("ultra", "Ультра"),
        ("custom", "Бизнес"),
    ]

    plane_type = models.CharField(max_length=16, choices=PLAN_TYPES)
    koefficient = models.DecimalField(max_digits=5, decimal_places=2)
    brief = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Тарифный план"
        verbose_name_plural = "Тарифные планы"
    
    def __str__(self):
        return f"Тарифный план {self.plane_type}"


class Consumer(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="consumers",
    )
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="consumers",
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name="consumers",
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "Потребитель"
        verbose_name_plural = "Потребители"
        indexes = [
            models.Index(fields=["client", "service", "plan"]),
        ]
    
    def __str__(self):
        return f"{self.client} {self.service} {self.plan}"
