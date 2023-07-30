from django.views.generic import DetailView

from .models import Task, TaskGroup


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskGroupDetailView(DetailView):
    model = TaskGroup
    template_name = 'task_group_detail.html'
    context_object_name = 'task_group'
