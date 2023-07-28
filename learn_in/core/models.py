from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание'
    )

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username


class Base(models.Model):

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
