from django.shortcuts import render
from .models import Item

# Create your views here.


def get_manager_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'manager/manager_list.html', context)
