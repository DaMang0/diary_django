from django.urls import include, path
from . import views
from .views import ArticleListView, ArticleCreate, ArticleDetail

urlpatterns = [
  # path('', views.home),
  path('article/create/', ArticleCreate.as_view(), name='article-create'),
  path('', ArticleListView.as_view(), name='article-list'),
  path('<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
  
]