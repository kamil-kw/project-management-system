from django import forms
from .models import Item


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(forms.ModelForm):
    """ form items """
    class Meta:
        model = Item
        fields = ['task', 'owner', 'due_date', 'done']
        widgets = {
            'due_date': DateInput(),
        }
