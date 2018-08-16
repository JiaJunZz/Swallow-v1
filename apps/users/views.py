from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from .forms import LoginForm

# Create your views here.

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            print(user_name,pass_word)
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                auth_login(request,user)
                return render(request,'index.html')
            else:
                return render(request, 'index.html',{"msg":"用户名密码错误"})

    elif request.method == "GET":
        return render(request,"login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




