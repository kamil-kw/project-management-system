"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_manager_list, name='get_manager_list'),
    path('add/', views.add_item, name='add'),

    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),
    path('accounts/', include('allauth.urls')),
    
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('add_project/', views.AddProject.as_view(), name='add_project'),
    path('update_project/<pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('delete_project/<pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
]
