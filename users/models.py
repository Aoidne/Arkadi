import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.conf import settings
from .managers import CustomUserManager


class CustomUser(AbstractUser):  # пользовательская модель
    email = models.EmailField(_("email address"), unique=True)


    USERNAME_FIELD = "email"  # задает имя поля в модели пользователя, которое используется в качестве уникального
    # идентификатора.
    REQUIRED_FIELDS = ["username"]  # Список имен полей, которые будут запрашиваться при создании суперпользователя
    # с помощью команды createsuperuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email


def get_image_filename(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_image_filename, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    birth_days = models.DateField(_("birth"), auto_now_add=True)

    def __str__(self):
        return self.user.email

    @property
    def filename(self):
        return os.path.basename(self.image.name)

