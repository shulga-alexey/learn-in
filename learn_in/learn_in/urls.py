from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls', namespace='users'))
]
