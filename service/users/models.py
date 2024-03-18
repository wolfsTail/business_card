from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from users.manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=128, blank=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(
        regex=r"^((\+7)|8)\d{10}$",
        message="Phone number must be entered in the format: '+79999999999' or '89999999999'.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=12, null=True, blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} {self.username if self.username else 'Unknown'}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
