from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

# Create your models here.
