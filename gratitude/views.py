from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView, CreateView, ListView, TemplateView, UpdateView
from .models import Gratitude_List
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import datetime
import calendar
from .forms import Gratitude_ListForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
  month_name = calendar.month_name[int(custom_month)]
  streak_count = 0
  compare_date = today + datetime.timedelta(1)

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
    
    return redirect("gratitude:date", year=today.year, month=today.month, day=today.day)

  user = get_object_or_404(User, pk=request.user.id)
  todays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=day)
  todays_list_count = todays_list.count()

  
  for xlist in list(user.gratitude_list_set.all().filter(date_created__lte=today).order_by('-date_created')):
    
    
    delta = compare_date - xlist.date_created
    
    if delta.days == 1:
      streak_count += 1
    elif delta.days == 0:
      pass
    else:
      break
    compare_date = xlist.date_created

    

  # yesterdays_list = user.gratitude_list_set.all().filter(date_created__year=year, date_created__month=month, date_created__day=path)
  context = {'todays_list_count': todays_list_count, 'streak_count': streak_count, 'month_name' :month_name, 'custom_page_date': custom_page_date, 'yesterday':yesterday, 'tomorrow':tomorrow, 'form': form, 'todays_list': todays_list, 'today': today, }
  return render(request, 'gratitude/date.html', context)


def gratitude_create_view(request):
  form = Gratitude_ListForm(request.POST or None)
  if form.is_valid():
    gratitude = form.save(commit=False)
    gratitude.user = request.user
    gratitude.save()
    
    return redirect("gratitude:date", year=today.year, month=today.month, day=today.day)
  
  context = {
    'form': form
    } 

  return render(request, 'gratitude/create.html', context)


class Delete(LoginRequiredMixin, DeleteView):
  model = Gratitude_List
  login_url='login'

  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(Gratitude_List, pk=pk_, user=self.request.user)
  
  def get_success_url(self):
    return reverse('gratitude:date', kwargs={'day': today.day, 'month': today.month, 'year': today.year,})


class Update(LoginRequiredMixin, UpdateView):
  login_url='login'
  model = Gratitude_List
  fields = ['title', ]
  template_name = "gratitude/update.html"

  def get_object(self):
    pk_ = self.kwargs.get("pk")
    return get_object_or_404(Gratitude_List, pk=pk_, user=self.request.user)

  def get_success_url(self):
    return reverse('gratitude:date', kwargs={'day': today.day, 'month': today.month, 'year': today.year,})


  

  