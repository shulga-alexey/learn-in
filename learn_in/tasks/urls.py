from django.urls import path
from .views import TaskDetailView, TaskGroupDetailView

app_name = 'tasks'

urlpatterns = [
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
