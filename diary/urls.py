from django.urls import include, path
from . import views
from .views import ArticleListView, ArticleCreate, ArticleDetail, ArticleDelete, ArticleUpdate, ArticleIndex

urlpatterns = [
  # path('', views.home),
  path('article/list/', ArticleListView.as_view(), name='article-list'),
  path('article/<slug:slug>/update/', ArticleUpdate.as_view(), name='article-update'),
  path('article/<slug:slug>/detail/', ArticleDetail.as_view(), name='article-detail'),
  path('article/create/', ArticleCreate.as_view(), name='article-create'),
  path('article/<slug:slug>/delete/', ArticleDelete.as_view(), name='article-delete'),
  path('', ArticleIndex.as_view(), name='article-index'),
  # path('<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
  
  
]