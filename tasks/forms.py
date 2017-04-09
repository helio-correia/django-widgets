from django import forms

from tasks.widgets import PickADateDateWidget
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {'due_date': PickADateDateWidget}
