from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, CustomSignUpForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


def SignUp(request):
  if request.method == 'POST':
    form = CustomSignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = CustomSignUpForm()
  context = {'form': form}
  return render(request, 'accounts/signup.html', context)

class Login(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_message = "Welcome "

class Profile(LoginRequiredMixin, DetailView):
  model = User
  login_url = 'login'
  redirect_field_name = 'user-profile'
  template_name = 'accounts/profile.html'

  def get_object(self):
    return self.request.user
