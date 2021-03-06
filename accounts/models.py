from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=25, default='anonymous')

  def __str__(self):
    return f"{self.user.username}'s Profile"

class Feedback(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  url = models.URLField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title