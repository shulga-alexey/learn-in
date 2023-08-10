from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """Настроенная модель пользователя."""

    class Role(models.TextChoices):
        """Статус пользователя: преподаватель/студент."""
        TEACHER = 'teacher'
        STUDENT = 'student'

    role = models.CharField(
        max_length=7,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name='роль'
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )

    class Meta:
        ordering = ('username',)

    def get_absolute_url(self):
        return reverse('users:user-detail', kwargs={'username': self.username})

    def __str__(self):
        return self.username


class Base(models.Model):
    """Базовый класс для задач, а также групп студентов и задач."""

    title = models.CharField(
        unique=True,
        max_length=250,
        verbose_name='название'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='слаг'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='дата обновления'
    )

    class Meta:
        abstract = True
        ordering = ('title',)

    def __str__(self):
        return self.title
