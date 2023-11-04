from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Student, Teacher


User = get_user_model()


class StudentForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ('first_name', 'last_name', 'username', 'email', 'role',)


class TeacherForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = ('first_name', 'last_name', 'username', 'email', 'role',)
