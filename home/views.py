from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import SinhVien
# Create your views here.

def index(request):
    return render(request, 'user/layouts/index.html')

def login(request):
    if request.method == 'POST':
            # username = request.POST.get('username')
        # password =  request.POST.get('password')

        # user = authenticate(request, username = username, password = password)

        # if user is not None:
        #     login(request, username)
        #     return redirect('home')
        # else:
        #     messages.info(request, 'Tài khoản không hợp lệ!')   
        if SinhVien.objects.filter(username = request.POST['username'], password = request.POST['password']).exists():
            sinhVien = SinhVien.objects.get(username= request.POST['username'], password = request.POST['password']) 
            return render(request ,'user/layouts/index.html', {'sinhVien' : sinhVien} )
        else:   
            messages.info(request, 'Tài Khoản không hợp lệ!')  
          
    return render(request, 'user/layouts/login.html')

def logOutUser(request):
    logout(request)
    return redirect('/')