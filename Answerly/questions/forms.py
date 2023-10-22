from django.forms import ModelForm
from .models import Question, Event
from django import forms


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['author', 'participants']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    