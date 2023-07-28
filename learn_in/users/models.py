from django.db import models

from core.models import Base, User


class StudentGroup(Base):
    """Учебная группа."""

    class Meta(Base.Meta):
        verbose_name = 'учебная группа'
        verbose_name_plural = 'учебные группы'


class Student(User):
    """Пользователь «student», студент."""

    student_groups = models.ManyToManyField(
        StudentGroup,
        blank=True,
        related_name='students',
        verbose_name='учебная группа'
    )

    class Meta(User.Meta):
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'


class Teacher(User):
    """Пользователь «teacher», преподаватель."""

    students = models.ManyToManyField(
        'Student',
        blank=True,
        related_name='teachers',
        verbose_name='студенты'
    )
    student_groups = models.ManyToManyField(
        'StudentGroup',
        blank=True,
        related_name='teachers',
        verbose_name='учебные группы'
    )

    class Meta(User.Meta):
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
