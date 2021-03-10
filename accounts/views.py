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


# Create your views here.
# def SignUp(request):
#   if request.method == 'POST':
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#       form.save()
#       username = form.cleaned_data.get('username')
#       Rpassword = form.cleaned_data.get('password')
#       user = authenticate(username=username, password=Rpassword)
#       login(request, user)
#       return redirect('article:list')
#   else:
#     form = UserCreationForm()
#   return render(request, 'registration/signup.html', {'form': form})

def CustomSignUp(request):
  if request.method == 'POST':
    form = CustomSignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = CustomSignUpForm()
  context = {'form': form}
  return render(request, 'registration/custom_register.html', context)

# class SignUpView(SuccessMessageMixin, CreateView):
#   form_class = SignUpForm
#   template_name = 'registration/signup.html'
#   success_url = reverse_lazy('login')
#   # success_message = "%(username)s was created successfully"

#   def get_success_message(self, cleaned_data):
#     print(cleaned_data)
#     return "Account Created!"


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'registration/login.html'
    success_message = "Welcome "

class UserAccount(DetailView):
  template_name = 'accounts/index.html'
  model = User

  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(User, pk=pk_)
    
  def get_context_data(self, **kwargs):
    pk_ = self.kwargs.get("pk")
    user = User.objects.get(id=pk_)
    context = super().get_context_data(**kwargs)   
    context['now'] = timezone.now()
    context['user_book'] = user.book_set.all()
    return context

class Profile(LoginRequiredMixin, DetailView):
  model = User
  login_url = 'login'
  redirect_field_name = 'user-profile'
  template_name = 'accounts/profile.html'

  def get_object(self):
    return self.request.user

class UserTasks(LoginRequiredMixin, DetailView):
  model = User
  login_url = 'login'
  redirect_field_name = 'user-task'
  template_name = 'accounts/user_tasks.html'

  def get_context_data(self, **kwargs):
    pk_ = self.kwargs.get("pk")
    user = User.objects.get(id=pk_)
    context = super().get_context_data(**kwargs) 
    context['tasks_count'] = user.tasks_set.count()
    return context
  # def get_context_data(self, **kwargs):
  #   user = User.objects.get(id=self.request.user.id)
  #   context = super().get_context_data(**kwargs) 
  #   context['tasks_count'] = user.tasks_set.count()
  #   return context
     
# You could try this 
# user = User.objects.get(username=request.user.username) 
# user = User.objects.get(pk=request.user.id)