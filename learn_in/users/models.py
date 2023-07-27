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


class Teacher(User):
    """Пользователь «teacher», преподаватель."""

    student_groups = models.ManyToManyField(
        'StudentGroup',
        blank=True,
        related_name='teachers',
        verbose_name='учебные группы'
    )
    students = models.ManyToManyField(
        'Student',
        blank=True,
        related_name='teachers',
        verbose_name='студенты'
    )

    class Meta(User.Meta):
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'


class Student(User):
    """Пользователь «student», студент."""

    student_groups = models.ManyToManyField(
        'StudentGroup',
        blank=True,
        related_name='students',
        verbose_name='учебная группа'
    )

    class Meta(User.Meta):
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'


class StudentGroup(models.Model):
    """Учебная группа."""

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

    class Meta:
        ordering = ('title',)
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'

    def __str__(self):
        return self.title
