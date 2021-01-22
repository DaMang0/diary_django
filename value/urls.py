from django.urls import path
from . import views

app_name = 'value'
urlpatterns = [
  path('', views.ValueIndex.as_view(), name='index'),
  path('<str:category>/', views.ValueTopicListView.as_view(), name='catecory-topic'),
  path('category/create/', views.CategoryCreateView.as_view(), name='catecory-create'),
  # path('create/', views.QuoteCreateView.as_view(), name='create'),
  # path('delete/<int:pk>/', views.QuoteDeleteView.as_view(), name='delete'),
]