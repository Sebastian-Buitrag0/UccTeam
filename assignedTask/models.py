from django.db import models
from task.models import Task    
from userTeam.models import UserTeam
# Create your models here.

class AssignedTask(models.Model):   
    fkTask = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    fkUserTeam = models.ForeignKey(UserTeam, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=64, null=False)

    def __str__(self): 
        return self.fkTask.name