from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  slug = models.SlugField(unique=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  # modified = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('article-list')

  # Set up unique slug field
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Article, self).save(*args, **kwargs)

