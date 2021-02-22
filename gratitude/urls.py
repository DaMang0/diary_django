from django.urls import path, register_converter
from . import views as gratitude_view
from datetime import datetime

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

app_name = 'gratitude'
urlpatterns = [
  path('list/<int:year>-<int:month>-<int:day>/', gratitude_view.Date, name='date'),
]



