from django.contrib import admin
from .models import Tasks, Genre, Book
# Register your models here.
admin.site.register(Tasks)
admin.site.register(Genre)
admin.site.register(Book)

