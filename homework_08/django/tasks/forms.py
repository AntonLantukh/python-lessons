from django.forms import DateField, DateInput, ModelForm, CharField, TextInput, ModelChoiceField, Textarea, TimeField, TimeInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'date',
            'time',
        ]

    title = CharField(
        label='Title',
        required=True,
        widget=TextInput(
            attrs={
                'placeholder': 'New task',
                'class': 'form-control',
            }
        )
    )

    description = CharField(
        label='Description',
        required=True,
        widget=Textarea(
            attrs={
                'placeholder': 'Task description',
                'rows': '5',
                'class': 'form-control',
            }
        )
    )

    date = DateField(
        label='Date',
        required=True,
        widget=DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        )
    )

    time = TimeField(
        label='Time',
        required=True,
        widget=TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
            }
        )
    )
