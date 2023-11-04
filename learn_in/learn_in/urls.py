from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from users.urls import authpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('auth/', include((authpatterns, 'users-app'), namespace='auth')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls', namespace='users')),
]
