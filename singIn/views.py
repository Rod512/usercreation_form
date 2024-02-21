from django.shortcuts import render, HttpResponseRedirect
from .forms import Singupforms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# sign_up
def sign_up(request):
    if request.method == 'POST':
        fm = Singupforms(request.POST)
        if fm.is_valid():
            messages.success(request,"Account created successfully")
            fm.save()
    else:
        fm = Singupforms()
    return render(request, 'singIn/index.html', {'form':fm})

# user_login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request= request, data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass, )
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'singIn/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/c')


# profile
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'singIn/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')