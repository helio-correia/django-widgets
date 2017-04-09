from django.contrib import admin

from .forms import TaskForm
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
