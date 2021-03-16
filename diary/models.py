from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
  CHOICES = (
    ('1', 'Article'),
    ('2', 'Creativity'),
    ('3', 'Diary'),
    ('4', 'Journal'),
    ('5', 'Knowledge'),
    ('6', 'Value'),
    )
  # article = models.ForeignKey(Article, on_delete=models.CASCADE)
  name = models.CharField(max_length=25, choices=CHOICES, unique=True, default='1')
  description = models.TextField(blank=True)

  def __str__(self):
    return self.get_name_display()

class Article(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100)
  body = RichTextField(blank=True, null=True)
  slug = models.SlugField(unique=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('article:list')

  # Set up unique slug field
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Article, self).save(*args, **kwargs)



class RichTextArticle(models.Model):
  title = models.CharField(max_length=75)
  body = RichTextField(blank=True, null=True)
  
  def __str__(self):
    return self.title

