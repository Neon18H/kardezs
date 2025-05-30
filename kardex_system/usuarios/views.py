from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm, LoginForm
from usuarios.services.Auth_service import AuthService
from usuarios.services.User_Service import  UserService

auth_service = AuthService()
user_service = UserService()

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user_service.register_user(request, form)
            return redirect('kardex')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth_service.login_user(request, username, password)
            if user:
                return redirect('kardex')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    auth_service.logout_user(request)
    return redirect('login')
