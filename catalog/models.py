from django.db import models
from wsgiref.validate import validator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=50, help_text="Напишите ФИО")
    username = models.CharField(max_length=50, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=254)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название категории")

    def __str__(self):
        return self.name


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    mb_limit = 2.0
    if filesize > mb_limit * 1024 * 1024:
        raise ValidationError("Размер изображения превышает 2MB!")


class Application(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название заявки")
    summary = models.TextField(max_length=1000, help_text="Опишите свою заявку здесь")
    caterogy = models.ForeignKey('Category', help_text='Выберите категория для заявки', on_delete=models.SET_NULL,
                                 null=True)
    image = models.ImageField(upload_to="images/", help_text="Максимальный размер изображения 2MB",
                              validators=[validate_image])
    time_stamp = models.DateTimeField(default=timezone.now())

    status_application = (
        ('n', 'Новая'),
        ('i', 'В процессе'),
        ('p', 'Выполнено'),
    )

    status = models.CharField(max_length=100, choices=status_application, blank=True, default="n")
    borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profile')
