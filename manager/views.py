from django.shortcuts import render, redirect
from .models import Item


# Create your views here.


def get_manager_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'manager/manager_list.html', context)


def add_item(request):
    if request.method == 'POST':
        task = request.POST.get('item_task')
        owner = request.POST.get('item_owner')
        done = 'done' in request.POST
        Item.objects.create(task=task, owner=owner, done=done)


        return redirect('get_manager_list')
    return render(request, 'manager/add_item.html')
