from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

#enum

class userStatus(Enum):
    MANAGER = 0
    EMPLOYEE  = 1

class taskStatus(Enum):
    NEW = 0
    RUNNING = 1
    FINISHED = 2

#models

class CustomUser(AbstractUser):
    userStatus = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in userStatus],
        default=userStatus.EMPLOYEE .value)
    phone=models.CharField(max_length=11,blank=True)
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='members'
    )

    def __str__(self):
        return self.username


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manager=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name='teams_managed',
        null=True,
        blank=True  )

    def clean(self):
        if self.manager:
            if self.manager.userStatus != 0:
                return("Manager must have MANAGER role")
            if self.manager.team and self.manager.team != self:
                return ("Manager must belong to this team")

    def __str__(self):
        return self.name



class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    goalDate=models.DateField()
    taskStatus = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in taskStatus],
        default=taskStatus.NEW.value)
    # המבצע בפועל – יכול להיות null אם עדיין לא שויך
    task_performer = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tasks_to_do'
    )
    # המנהל האחראי על המשימה
    task_manager = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='tasks_managed'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='tasks'
    )
    def __str__(self):
        return self.title







