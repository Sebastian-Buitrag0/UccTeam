from django.db import models

# Create your models here.

class Team(models.Model):   
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    creationDate = models.DateField()

    def __str__(self):
        return self.name
    
    