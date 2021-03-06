import django_filters
from django_filters import DateFilter, CharFilter
from .models import Item
from .forms import DateInput


class DueDateFilter(django_filters.FilterSet):
    """[Filter fields]"""
    project = CharFilter(field_name="project",
                         lookup_expr="icontains",
                         label="Project")
    start_date = DateFilter(field_name="due_date",
                            lookup_expr="gte",
                            label="Due date start",
                            widget=DateInput(attrs={'type': 'date'}))
    end_date = DateFilter(field_name="due_date",
                          lookup_expr="lte",
                          label="Due date end",
                          widget=DateInput(attrs={'type': 'date'}))
    owner = CharFilter(field_name="owner",
                       lookup_expr="icontains",
                       label="Owner")

    class Meta:
        """[remain filters fields]"""
        model = Item
        fields = '__all__'
        exclude = ['project', 'task', 'owner', 'due_date']
