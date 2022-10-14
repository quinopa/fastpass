from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
from . import forms, models
from .helper_functions import encrypt, decrypt

key = b'WS3nqyK86B35RdDKTcxZcXCa64haA_bP7CdHgYMm3es='

# Create your views here.
@login_required
def home(request):
    passwords = models.PasswordModel.objects.filter(password_user=request.user)
    return render(request, "passwords/home.html", context={"passwords": passwords})

@login_required
def password(request, password_id):
    password = models.PasswordModel.objects.get(id=password_id)
    if password.password_user != request.user:
        return redirect('home')

    decoded = decrypt(key, password.password).decode()

    return render(request, "passwords/password.html", context={"password": password, "decoded": decoded})

@login_required
def create(request):
    if request.method == "POST":
        form = forms.PasswordForm(request.POST)
        if form.is_valid():
            password: str = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            entry = models.PasswordModel(name=name, password=encrypt(key, password.encode()), password_user=request.user)
            entry.save()
            return redirect("password-home")
    else:
        form = forms.PasswordForm()

    return render(request, "passwords/create.html", {'form': form})

@login_required()
def delete(request, password_id):
    password = models.PasswordModel.objects.get(id=password_id)
    if password.password_user != request.user:
        return redirect('home')

    password.delete()
    return redirect('password-home')