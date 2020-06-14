from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import SinhVien, TheLoai, TopSach, TacGia, NhaXuatBan, Sach
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    theLoai = TheLoai.objects.all()
    topSach = TopSach.objects.all()[0:1]
    topSachR = TopSach.objects.all()[1:5]
    tacgia = TacGia.objects.all();
    nxb = NhaXuatBan.objects.all();
    return render(request, 'user/layouts/index.html', {'theloai' : theLoai , 'topsach' : topSach, 'topR' : topSachR, 'tg' : tacgia, 'nxb' : nxb})

def login(request):
    if request.method == 'POST':
        if SinhVien.objects.filter(username = request.POST['username'], password = request.POST['password']).exists():
            sinhVien = SinhVien.objects.get(username= request.POST['username'], password = request.POST['password'])
            theLoai = TheLoai.objects.all()
            topSach = TopSach.objects.all()[0:1]
            topSachR = TopSach.objects.all()[1:5]
            tacgia = TacGia.objects.all();
            nxb = NhaXuatBan.objects.all();
            return render(request, 'user/layouts/index.html', {'theloai' : theLoai , 'topsach' : topSach, 'topR' : topSachR, 'tg' : tacgia, 'nxb' : nxb,'sinhVien' : sinhVien}) 
           
        else:   
            messages.info(request, 'Tài Khoản không hợp lệ!')  
    return render(request, 'user/layouts/login.html')

def logOutUser(request):
    logout(request)
    return redirect('home')

def theLoai(request, id):
    theLoai = TheLoai.objects.filter(ma_TheLoai = id)
    topSach = TopSach.objects.all()[0:1]
    topSachR = TopSach.objects.all()[1:5]
    tacgia = TacGia.objects.all();
    nxb = NhaXuatBan.objects.all();
    sach = Sach.objects.filter(loaiSach = id)
    return render(request, 'user/layouts/category.html', {'theloai' : theLoai , 'topsach' : topSach, 'topR' : topSachR, 'tg' : tacgia, 'nxb' : nxb, 's' : sach})

def yeuCau(request, id):
    sach = Sach.objects.filter(ma_Sach = id)
    return render(request, 'user/layouts/yeucau.html',{'s' : sach})