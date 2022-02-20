import django_filters
from django_filters import DateFilter, CharFilter

from .models import Item


# class OrderFilter(django_filters.FilterSet):
#     start_date = DateFilter(field_name="due_date", lookup_expr="gte")
#     end_date = DateFilter(field_name="due_date", lookup_expr="lte")
#     class Meta:
#         model = Item
#         fields = '__all__'
#         exclude = ['due_date', 'task']
        

class DueDateFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="due_date", lookup_expr="gte")
    end_date = DateFilter(field_name="due_date", lookup_expr="lte")
    owner = CharFilter(field_name="owner", lookup_expr="icontains")
