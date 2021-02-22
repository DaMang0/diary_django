from django import forms
from .models import Gratitude_List

class Gratitude_ListForm(forms.ModelForm):
  class Meta:
    models = Gratitude_List
    fields = '__all__'