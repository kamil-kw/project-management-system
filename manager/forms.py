from django import forms
from .models import Item, Project


class ProjectChoices(forms.ModelForm):
    """[Project Choices ]"""
    project_choices = Project.objects.all().values_list('name', 'name')
    project_list = []
    for choice in project_choices:
        project_list.append(choice)


class DateInput(forms.DateInput):
    """[to define input type for calendar picker]"""
    input_type = 'date'


class ItemForm(forms.ModelForm):
    """ form items """
    class Meta:
        """[ fields list and widget ]"""
        model = Item

        fields = ['project', 'task', 'owner', 'due_date', 'done']
        widgets = {
            'due_date': DateInput(attrs={'class': 'form-control'}),
            'task': forms.Textarea(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'project' : forms.Select(choices = ProjectChoices.project_list, 
                                     attrs={'class': 'form-control'}),
        }