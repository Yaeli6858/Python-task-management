from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task, CustomUser


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'goalDate', 'task_performer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task_performer'].required = False


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "phone", "email")


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = (
        ('', 'All'),
        ('0', 'New'),
        ('1', 'In Progress'),
        ('2', 'Completed'),
    )

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    assigned = forms.ChoiceField(
        choices=(('', 'All'), ('assigned', 'Assigned'), ('unassigned', 'Unassigned')),
        required=False
    )
    worker_id = forms.ChoiceField(choices=[], required=False)

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.team:
            self.fields['worker_id'].choices = [('', 'All')] + [
                (member.id, member.username) for member in user.team.members.all()
            ]