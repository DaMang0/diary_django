from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView, TemplateView
from .models import Gratitude_List
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
from .forms import Gratitude_ListForm
# Create your views here.

today = datetime.date.today()
# yesterday = today - datetime.timedelta(days=1)
year = today.year
month = today.month
day = today.day
# yyear = yesterday.year
# ymonth = yesterday.month
# yday = yesterday.day

def Date(request, year, month, day):
  user = get_object_or_404(User, pk=request.user.id)
  todays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=day)
  # yesterdays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=yday)
  context = {'todays_list': todays_list, 'year': year, 'month': month, 'day': day}
  return render(request, 'gratitude/date.html', context)

def gratitude_create_view(request):
  form = Gratitude_ListForm(request.POST or None)
  if form.is_valid():
    gratitude = form.save(commit=False)
    gratitude.user = request.user
    gratitude.save()
    
    return redirect("gratitude:date", year=year, month=month, day=day)
  
  context = {
    'form': form
    } 

  return render(request, 'gratitude/create.html', context)