from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'user/layouts/main.html')

