from django.db import IntegrityError

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # Inserts into DB
                user.save()
                # Login user
                login(request, user)
                # Redirect to currenttodos and return render
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Passwords did not match'})


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')