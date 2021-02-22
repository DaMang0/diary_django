from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, CreateView, ListView, TemplateView
from .models import Gratitude_List
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from datetime import date
# Create your views here.


def Date(request, year, month, day):
  user = get_object_or_404(User, pk=request.user.id)
  todays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=day)
  context = {'todays_list': todays_list, 'year': year, 'month': month, 'day': day,}
  return render(request, 'gratitude/date.html', context)