from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from utils.send_email import send_email
from random import randint
from .models import Code



def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            code = randint(10000,99999)
            Code.objects.create(user = user, code = code)
            send_email(form.cleaned_data.get("email"),code)
            return redirect("verify_email")
        else:
            messages.add_message(request,messages.ERROR,form.errors)

    return render(request,'register.html')


@login_required(login_url='login')
def verify_email(request):

    if request.method == "POST":
        code = request.POST.get('code')

        if Code.objects.filter(user = request.user,code = code).exists():
            return redirect("home")
        else:
            messages.add_message(request,messages.ERROR,"code is invalid")

    return render(request,'verify_email.html')

def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.add_message(request,messages.ERROR,'User not found')
        
        else:
            messages.add_message(request,messages.ERROR,form.errors)

    return render(request,'login.html')                        