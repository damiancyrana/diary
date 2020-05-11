from django.shortcuts import render
from .models import Subject


def index(request):
    return render(request, 'index.html')


def subjects(request):
    subjects = Subject.objects.order_by('addition_time')
    context = {'subjects': subjects}
    return render(request, 'subject/subjects.html', context)


def subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    entries = subject.entry_set.order_by('-addition_time')
    context = {'subject': subject, 'entries': entries}
    return render(request, 'subject/subject.html', context)
