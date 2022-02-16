from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Item, Project
from .forms import ItemForm


# Create your views here.
""" using classes"""

class HomeView(ListView):
    """[add home view template]"""
    model = ItemForm
    template_name = 'manager/manager_list.html'


class AddProject(CreateView):
    """ add project function """
    model = Project
    template_name = 'manager/add_project.html'
    fields = '__all__'


def get_manager_list(request):
    """ manager list """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'manager/manager_list.html', context)


def add_item(request):
    """ add item function """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_manager_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'manager/add_item.html', context)


def edit_item(request, item_id):
    """ edit item function """
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_manager_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'manager/edit_item.html', context)


def toggle_item(request, item_id):
    """ toggle items """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_manager_list')


def delete_item(request, item_id):
    """ delete items """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_manager_list')

