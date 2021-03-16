from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, FeedbackForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Feedback


def SignUp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = SignUpForm()
  context = {'form': form}
  return render(request, 'accounts/signup.html', context)

class Login(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    success_message = "Welcome "
    redirect_authenticated_user = True

    

class Profile(LoginRequiredMixin, DetailView):
  model = User
  login_url = 'login'
  redirect_field_name = 'user-profile'
  template_name = 'accounts/profile.html'

  def get_object(self):
    return self.request.user

class Feedback(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Feedback
  form_class = FeedbackForm
  # fields = ['title', 'body', 'url']
  template_name = 'accounts/feedback.html'
  success_url = reverse_lazy('article:list')
  success_message = "Thank you for the feedback, we are always trying our best to provide you the best experience possible."

  def form_valid(self, form):
      obj = form.save(commit=False)
      obj.user = self.request.user
      obj.save()
      return HttpResponseRedirect(reverse('article:list'))