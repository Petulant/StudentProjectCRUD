from django.db import models

# Create your models here.

class groupProjects(models.Model):
       pid = models.CharField(max_length=4)
       projectName = models.CharField(max_length=225)
       uploadedBy = models.CharField(max_length=100)
       subDate = models.DateField(null=True)
       
       def __str__(self):
           return self.projectName 