from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import StudentGroup

User = get_user_model()


class StudentGroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'student_group_detail.html'
    context_object_name = 'student_group'


class UserDetailView(DetailView):

    def get_queryset(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_object(self):
        return getattr(self.get_queryset(), self.kwargs.get('status'))

    def get_template_names(self):
        return self.kwargs.get('status') + '_detail.html'

    def get_context_object_name(self, obj):
        return self.kwargs.get('status')
