from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        AGENT = "agent", "Agent"
        USER = "user", "User"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_agent(self):
        return self.role in (self.Role.ADMIN, self.Role.AGENT)