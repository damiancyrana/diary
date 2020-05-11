from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('diary:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('diary:index'))

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
