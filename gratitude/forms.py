from django import forms
from .models import Gratitude_List

class Gratitude_ListForm(forms.ModelForm):
  class Meta:
    model = Gratitude_List
    fields = '__all__'
    exclude = ('user',)