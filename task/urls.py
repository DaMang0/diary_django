from . import views as task_views
from django.urls import path

urlpatterns = [
    path('delete/<int:pk>/', task_views.DeleteTask.as_view(), name='task-delete'),
    
]