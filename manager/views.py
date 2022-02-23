from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Item, Project
from .forms import ItemForm
from .filters import DueDateFilter


# Create your views here. """ using classes"""

class HomeView(ListView):
    """[add home view template]"""
    model = Item
    template_name = 'manager/manager_list.html'
    ordering = ['due_date']


class ProjectView(ListView):
    """[project view template]"""
    model = Project
    template_name = 'manager/projects.html'


class AddProject(CreateView):
    """ add project function """
    model = Project
    template_name = 'manager/add_project.html'
    fields = '__all__'
    

class ProjectUpdateView(UpdateView):
    """ add project function """
    model = Project
    template_name = 'manager/update_project.html'
    fields = '__all__'


class ProjectDeleteView(DeleteView):
    """ add project function """
    model = Project
    template_name = 'manager/delete_project.html'
    success_url = reverse_lazy('get_manager_list')


def get_manager_list(request):
    """ manager list view"""
    context = {}
    my_filter = DueDateFilter(request.GET, queryset= Item.objects.all().order_by('due_date'), )
    context['my_filter'] = my_filter
    paginated_filtered = Paginator(my_filter.qs, 7)
    page = request.GET.get('page')
    page_items = paginated_filtered.get_page(page)
    context['page_items'] = page_items
    return render(request, 'manager/manager_list.html', context=context)


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

