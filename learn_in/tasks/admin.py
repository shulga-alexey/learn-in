from django.contrib import admin

from .models import Task, TaskGroup


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'producer_teacher', 'status', 'get_task_groups')
    list_filter = ('producer_teacher', 'status')
    search_fields = ('title',)
    ordering = ('producer_teacher', 'title', 'status')

    @admin.display(description='группы задач')
    def get_task_groups(self, obj):
        return ',\n'.join(item.title for item in obj.task_groups.all())


@admin.register(TaskGroup)
class TaskGroupAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created')
    search_fields = ('title', 'slug')
    ordering = ('title',)
    empty_value_display = '-empty-'
