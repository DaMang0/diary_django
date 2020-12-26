from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100, default='title')
  content = models.TextField()
  slug = models.SlugField(unique=True)
  pub_date = models.DateTimeField(default=timezone.now)