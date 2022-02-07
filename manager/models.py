from django.db import models

# Create your models here.

class task_item(models.Model):
    task = models.CharField(max_length=300, null=False, blank=False)
    owner = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    

