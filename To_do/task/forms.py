from django import forms
from django.core.exceptions import ValidationError

from helpers.choices import STATUS_CHOICES
from task.models import Task


class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError('Name should contain only letters!!')


        task= Task.objects.filter(name=name)
        if task:
            raise ValidationError('Task with this Name already excist!!')

        return name