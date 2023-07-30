from django.urls import path
from .views import StudentGroupDetailView, UserDetailView

app_name = 'users'

urlpatterns = [
    path(
        'student-group/<slug:slug>/',
        StudentGroupDetailView.as_view(),
        name='student-group'
    ),
    path(
        '<str:status>/<str:username>/',
        UserDetailView.as_view(),
        name='user'
    ),
]
