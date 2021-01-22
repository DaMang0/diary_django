from django.db import models

class Topic(models.Model):
  category = models.ForeignKey('Category', related_name='related_topic',  on_delete=models.CASCADE, null=True)
  header = models.CharField(max_length=100, unique=True, null=True)
  content = models.TextField(null=True)

  def __str__(self):
    return f"{self.header}"


# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50, unique=True, null=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('value:catecory-topic')

# class Topic(models.Model):
#   topic_category = models.ForeignKey(Category, on_delete=models.CASCADE)
#   header = models.CharField(max_length=100, unique=True)
#   text = models.TextField()

#   def __str__(self):
#     return f"{self.header}. ({self.topic_category})"


# class Student(models.Model):
#   name = models.CharField(max_length=100)
#   major = models.ForeignKey('Degree', related_name='student_major', on_delete=models.CASCADE)

#   def __str__(self):
#     return self.name

# class Degree(models.Model):
#   name = models.CharField(max_length=100)

#   def __str__(self):
#     return self.name
