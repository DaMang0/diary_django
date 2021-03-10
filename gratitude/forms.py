from django import forms
from .models import Gratitude_List
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin
class Gratitude_ListForm(forms.ModelForm):
  title = forms.CharField(label=False)
  class Meta:
    model = Gratitude_List
    fields = '__all__'
    exclude = ('user',)