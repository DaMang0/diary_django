from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView, CreateView
from .models import Tasks
from django.urls import reverse_lazy, reverse


# Create your views here.

class TaskList(DetailView):
  template_name = 'task/tasks_list.html'
  queryset = User.objects.all()
  
  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(User, id=pk_)

class DeleteTask(DeleteView):
  model = Tasks
  success_url = 'user-task'
  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(Tasks, pk=pk_)

  # def get_success_url(self, **kwargs):
  #   # Return Back to User Profile Task Page after deleting a task
  #   return reverse("account-profile", kwargs={'pk': self.request.user.pk})

