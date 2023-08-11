from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView

from .models import Student, StudentGroup, Teacher
from .forms import StudentForm, TeacherForm

User = get_user_model()


class SignUp(CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('index')
    template_name = 'auth/signup.html'

    def form_valid(self, form):
        if form.is_valid():
            if form.cleaned_data['role'] == 'student':
                form.save()
            else:
                TeacherForm(self.request.POST).save()
        return redirect(self.success_url)


class UserDetailView(DetailView):

    def get_queryset(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_object(self):
        user = self.get_queryset()
        return getattr(user, 'student', getattr(user, 'teacher', None))

    def get_template_names(self):
        return 'users/' + self.object.role + '_detail.html'

    def get_context_object_name(self, obj):
        return obj.role


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all()
        context['students'] = Student.objects.all()
        context['student_groups'] = StudentGroup.objects.all()
        return context


class StudentGroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'users/student_group_detail.html'
    context_object_name = 'student_group'
