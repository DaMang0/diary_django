# from django.db import models
# from django.urls import reverse

# class Quote(models.Model):
#   message = models.CharField(max_length=255)
#   created = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.message

#   # Return to quote index page after creation
#   def get_absolute_url(self):
#     return reverse('quotes:index')