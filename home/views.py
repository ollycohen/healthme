from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/signup')
def home(request):
    return render(request, 'home/home.html', {})
