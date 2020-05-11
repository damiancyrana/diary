from django import forms
from .models import Subject, Entry


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}
