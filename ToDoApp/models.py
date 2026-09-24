from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model): 
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task_name = models.CharField(max_length = 200)
    task_completed = models.BooleanField(default = False)
    task_created_at = models.DateTimeField(auto_now_add = True)
    task_deadline = models.DateTimeField(null = True, blank = True)


    def __str__(self):
        return self.task_name

    @property
    def is_overdue(self):
        if self.task_deadline and not self.task_completed:
            return timezone.now() > self.task_deadline
        return False