from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gratitude_List(models.Model):
  title = models.CharField(max_length=100, unique=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  date_created = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.title