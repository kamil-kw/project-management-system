from django.shortcuts import render

# Create your views here.
def get_manager_list(request):
    return render(request, 'manager/manager_list.html')

