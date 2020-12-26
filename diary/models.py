from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100, default='title')
  content = models.TextField()
  slug = models.SlugField(unique=True, default='Not provided')
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('article-list')