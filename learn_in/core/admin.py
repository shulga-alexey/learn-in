from django.contrib import admin

from .models import User


@admin.register(User)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ('username', 'email')
