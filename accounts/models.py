from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SCHOOL_ADMIN = "school_admin", "School admin"
        PARENT = "parent", "Parent"
        DRIVER = "driver", "Driver"
        MARSHAL = "marshal", "Marshal"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PARENT)
    phone = models.CharField(max_length=20, blank=True, help_text="Used for notifications")
    # `school` FK is added in Week 2, alongside the schools app.

    @property
    def is_school_admin(self):
        return self.role == self.Role.SCHOOL_ADMIN

    @property
    def is_parent(self):
        return self.role == self.Role.PARENT

    @property
    def is_driver(self):
        return self.role == self.Role.DRIVER

    @property
    def is_marshal(self):
        return self.role == self.Role.MARSHAL
