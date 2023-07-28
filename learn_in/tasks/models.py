from django.db import models
from django.urls import reverse

from core.models import Base
from users.models import Teacher, Student


class AcceptedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Task.Status.ACCEPTED)


class TaskGroup(Base):

    class Meta(Base.Meta):
        verbose_name = 'группа задач'
        verbose_name_plural = 'группы задач'


class Task(Base):

    class Status(models.TextChoices):
        """Статус задачи: разрешена/отклонена для публикации."""
        REJECTED = 'RJ', 'Rejected'
        ACCEPTED = 'AC', 'Accepted'

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.REJECTED,
        verbose_name='статус'
    )
    producer_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='produced_tasks',
        verbose_name='создавший'
    )
    appointor_teachers = models.ManyToManyField(
        Teacher,
        through='AppointedTask',
        through_fields=('task', 'appointor_teacher'),
        related_name='appointed_tasks',
        verbose_name='назначившие'
    )
    students = models.ManyToManyField(
        Student,
        through='AppointedTask',
        through_fields=('task', 'student'),
        related_name='tasks',
        verbose_name='студенты'
    )
    task_groups = models.ManyToManyField(
        TaskGroup,
        blank=True,
        related_name='tasks',
        verbose_name='группы задач'
    )

    objects = models.Manager()
    accepted = AcceptedManager()

    class Meta(Base.Meta):
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=(self.slug,))


class AppointedTask(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name='задача'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='студент'
    )
    appointor_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='назначивший'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )
    deadline = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата сдачи'
    )
