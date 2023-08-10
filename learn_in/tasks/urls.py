from django.urls import path
from .views import TaskDetailView, TaskGroupDetailView, TaskListView

app_name = 'tasks'

urlpatterns = [
    path(
        '',
        TaskListView.as_view(),
        name='task-list'
    ),
    path(
        'task/<slug:slug>/',
        TaskDetailView.as_view(),
        name='task-detail'
    ),
    path(
        'task-group/<slug:slug>/',
        TaskGroupDetailView.as_view(),
        name='task-group'
    ),
]
