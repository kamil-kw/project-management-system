from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    """ Projects list """
    name = models.CharField(max_length=300)
    
    def __str__(self):
        """[class objects as a string]"""
        return self.name

    def get_absolute_url(self):
        """[define absolute url for views classes]"""
        return reverse('get_manager_list')


class Item(models.Model):
    """ Project task list items """
    project = models.CharField(max_length=300, default='Not assigned')
    task = models.CharField(max_length=300, null=False, blank=False)
    due_date = models.DateTimeField(null=False)
    owner = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.task
