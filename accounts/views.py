from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView
from .models import Profile, User
from .forms import SignUpForm
from django.urls import reverse_lazy
class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name='accounts/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('events:list')


class ProfileView(DetailView):
    model=Profile
    template_name='accounts/profile.html'

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model=Profile
    fields=('bio', 'profile_image')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model=Profile
    success_url= reverse_lazy('accounts:logout')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)
