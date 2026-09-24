from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_deadline'] #doar campurile pe care le completeaza utilizatorul  
        labels = {
            'task_name': 'Task Name', 
            'task_deadline': 'Task Deadline', 
        }
        widgets = {
            'task_name': forms.TextInput(
                attrs = {
                    'placeholder': 'e.g. Water the flowers',
                    'class': 'form-control'
                }
            ),
            'task_deadline': forms.DateTimeInput(
                attrs = {
                    'type': 'datetime-local', 
                    'class': 'form-control'
                }
            ),  
        }