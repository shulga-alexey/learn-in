from django.contrib import admin

from .models import Student, StudentGroup, Teacher


class UserAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'username', 'email', 'get_student_groups')
    search_fields = ('full_name', 'username', 'email')
    ordering = ()
    empty_value_display = '-empty-'

    @admin.display(ordering='full_name', description='имя')
    def full_name(self, obj):
        return obj.user_ptr.get_full_name()

    @admin.display
    def username(self, obj):
        return obj.user_ptr

    @admin.display
    def email(self, obj):
        return obj.user_ptr.email

    @admin.display(description='учебные группы')
    def get_student_groups(self, obj):
        return ',\n'.join(item.title for item in obj.student_groups.all())


class GroupAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'get_teachers', 'created')
    search_fields = ('title', 'slug')
    ordering = ('title',)
    empty_value_display = '-empty-'

    @admin.display(description='преподаватели')
    def get_teachers(self, obj):
        return ',\n'.join(
            item.user_ptr.get_full_name() for item in obj.teachers.all()
        )


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):

    pass


@admin.register(Student)
class StudentAdmin(UserAdmin, GroupAdmin):

    list_display = UserAdmin.list_display + ('get_teachers',)


@admin.register(StudentGroup)
class StudentGroupAdmin(GroupAdmin):

    pass
