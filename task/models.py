from django.db import models
from user.models import User
# Create your models here.

class Task(models.Model):  
    title = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=256, null=False)
    expiratioDate= models.DateField()
    state = models.CharField(max_length=40, default="Pendiente")
    fkUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title+" -> " +self.state