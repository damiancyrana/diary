from django.shortcuts import render
from .models import Subject
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SubjectForm, EntryForm
from .models import Subject, Entry


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


def new_subject(request):
    if request.method != 'POST':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diary:subjects'))
    contex = {'form': form}
    return render(request, 'subject/new_subject.html', contex)


def new_entry(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.subject = subject
            new_entry.svae()
            return HttpResponseRedirect(reverse('diary:subject', args=[subject_id]))
    context = {'subject': subject, 'form': form}
    return render(request, 'subject/new_subject.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    subject = entry.subject
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diary:subject', args=[subject.id]))
    context = {'entry': entry, 'subject': subject, 'form': form}
    return render(request, 'entry/edit_entry.html', context)
