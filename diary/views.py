from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import SubjectForm, EntryForm
from .models import Subject, Entry
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def subjects(request):
    subjects = Subject.objects.filter(owner=request.user).order_by('addition_time')
    context = {'subjects': subjects}
    return render(request, 'subject/subjects.html', context)


@login_required
def subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if subject.owner != request.user:
        raise Http404

    entries = subject.entry_set.order_by('-addition_time')
    context = {'subject': subject, 'entries': entries}
    return render(request, 'subject/subject.html', context)


@login_required
def new_subject(request):
    if request.method != 'POST':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_subject = form.save(commit=False)
            new_subject.owner = request.user
            new_subject.save()
            return HttpResponseRedirect(reverse('diary:subjects'))

    contex = {'form': form}
    return render(request, 'subject/new_subject.html', contex)


@login_required
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


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    subject = entry.subject
    if subject.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diary:subject', args=[subject.id]))

    context = {'entry': entry, 'subject': subject, 'form': form}
    return render(request, 'entry/edit_entry.html', context)
