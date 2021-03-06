from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# a lot of code for authentication taken from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

# doing signup in auth instead


def signup(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect('/?first_login=true')
        else:
            messages.error(request, "There was an error with your signup form")
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})


def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect('/?first_login=false')
        else:
            messages.error(request, "There was an error with your login form")
    else:
        form = AuthenticationForm(request)

    return render(request, 'auth/login.html', {'form': form})
