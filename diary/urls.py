from django.urls import include, path
from . import views
from .views import ArticleListView, ArticleCreate, ArticleDetail, ArticleDelete, ArticleUpdate

urlpatterns = [
  # path('', views.home),
  path('article/<slug:slug>/update/', ArticleUpdate.as_view(), name='article-update'),
  path('article/<slug:slug>/detail/', ArticleDetail.as_view(), name='article-detail'),
  path('article/create/', ArticleCreate.as_view(), name='article-create'),
  path('article/<slug:slug>/delete/', ArticleDelete.as_view(), name='article-delete'),
  path('', ArticleListView.as_view(), name='article-list'),
  # path('<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
  
  
]