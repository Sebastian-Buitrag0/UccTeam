from django.db import models
from user.models import User
from team.models import Team

# Create your models here.

class UserTeam(models.Model):   
    fkUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    fkTeam = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    isLeader = models.BooleanField(null=False)
    isMember = models.BooleanField(null=False)
    isCreator = models.BooleanField(null=False) 

    def __str__(self):
        return self.fkUser.username+" ->" +self.fkTeam.name