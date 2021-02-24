from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView, TemplateView
from .models import Gratitude_List
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
from .forms import Gratitude_ListForm
from django.contrib.auth.decorators import login_required


today = datetime.date.today()
year = today.year
month = today.month
day = today.day

@login_required(login_url='login')
def Date(request, year, month, day):
  form = Gratitude_ListForm(request.POST or None)
  # Getting the current URL path
  path = request.path

  # Slicing and getting the day month year detail from the URL path
  custom_year = path.split('-')[0][-4:]
  custom_month = path.split('-')[1]
  custom_day = path.split('-')[2][:-1]

  # Check if all custom date variables contain decimal ONLY
  if custom_year.isdecimal() and custom_month.isdecimal() and custom_year.isdecimal:
    custom_page_date = today
    custom_page_date = custom_page_date.replace(year=int(custom_year), month=int(custom_month), day=int(custom_day))
    yesterday = custom_page_date - datetime.timedelta(days=1)
    tomorrow = custom_page_date + datetime.timedelta(days=1)
  else:
    yesterday = today
    tomorrow = today
  
  if form.is_valid():
    gratitude = form.save(commit=False)
    gratitude.user = request.user
    gratitude.save()
    
    return redirect("gratitude:date", year=year, month=month, day=day)

  user = get_object_or_404(User, pk=request.user.id)
  todays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=day)
  # yesterdays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=path)
  context = {'custom_page_date': custom_page_date,'yesterday':yesterday.day, 'yestermonth':yesterday.month, 'yesteryear':yesterday.year, 'tomorrowday':tomorrow.day, 'tomorrowmonth':tomorrow.month, 'tomorrowyear':tomorrow.year, 'form': form, 'todays_list': todays_list, 'year': year, 'month': month, 'day': day}
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
