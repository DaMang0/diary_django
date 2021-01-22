from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def SignUp(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      Rpassword = form.cleaned_data.get('password')
      user = authenticate(username=username, password=Rpassword)
      login(request, user)
      return redirect('article-list')
  else:
    form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form})

class SignUpView(SuccessMessageMixin, CreateView):
  form_class = UserCreationForm
  template_name = 'registration/signup.html'
  success_url = reverse_lazy('login')
  # success_message = "%(username)s was created successfully"

  def get_success_message(self, cleaned_data):
    print(cleaned_data)
    return "Account Created!"

class AccountDetailView(DetailView):
  template_name = 'accounts/index.html'
  model = User
  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(User, pk=pk_)