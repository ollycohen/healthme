from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# a lot of code for authentication taken from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

# doing signup in auth instead
def signup(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("VALID FORM!")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            # redirect to the page the user wanted to access if there was one
            if request.GET.get('next') != None:
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return render(request, '/home/home.html', {})
        else:
            print("INVALID FORM")
    else:
        print("NO POST")
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})
def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm(request)

    return render(request, 'auth/login.html', {'form': form})