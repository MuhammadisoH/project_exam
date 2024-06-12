from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import KirimForm
from .models import Kirim

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','last_name':'','first_name':'', 'password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@login_required
def chiqimlar_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'chiqimlar.html', {'form': form})

@login_required
def kirimlar_view(request):
    if request.method == 'POST':
        form = KirimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kirimlar')
    else:
        form = KirimForm()
    
    kirimlar = Kirim.objects.all()
    return render(request, 'kirimlar.html', {'form': form, 'kirimlar': kirimlar})

def delete_kirim_view(request, id):
    kirim = Kirim.objects.get(id=id)
    kirim.delete()
    return redirect('kirimlar')


@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def chiqimlar_view(request):
    return render(request, 'auth/chiqimlar.html')

def kirimlar_view(request):
    return render(request, 'auth/kirimlar.html')

def hisobotlar_view(request):
    return render(request, 'auth/hisobotlar.html')