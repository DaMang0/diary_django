from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.

class Tasks(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100)
  content = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

  def __str__(self):
    return f"{self.title} - User: {self.user.username}"


class Genre(models.Model):
  name = models.CharField(max_length=25)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  genre = models.ManyToManyField(Genre)
  
  def __str__(self):
    return f"{self.title}. by {self.author.username}" 





