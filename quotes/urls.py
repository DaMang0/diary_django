from django.urls import path
from . import views

app_name = 'quotes'
urlpatterns = [
  path('', views.QuoteListView.as_view(), name='index'),
  path('create/', views.QuoteCreateView.as_view(), name='create'),
  path('delete/<int:pk>/', views.QuoteDeleteView.as_view(), name='delete'),
]