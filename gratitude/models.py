from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gratitude_List(models.Model):
  title = models.CharField(max_length=255, unique=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  date_created = models.DateField(auto_now_add=True)
  time_created = models.DateTimeField(auto_now_add=True, null=True)
  edited = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title