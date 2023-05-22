import uuid
import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from webuser.manager import CustomUserManager
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class WebUser(AbstractBaseUser, PermissionsMixin):
    cognito_id = models.UUIDField(editable=False, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    last_active = models.DateTimeField(auto_now=True, null=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name", default="")
    last_name = models.CharField(max_length=100, verbose_name="Last Name", default="")
    email = models.EmailField(_("Email address"), unique=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
