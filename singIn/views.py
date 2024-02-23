from django.shortcuts import render, HttpResponseRedirect
from .forms import Singupforms,EdituserProfile,EditadminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User


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
        return HttpResponseRedirect('/profile/')


# profile
def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditadminProfile(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = EdituserProfile(request.POST, instance = request.user)
            if fm.is_valid:
                messages.success(request, 'Profile Updates')
                fm.save()
               
        else:
            if request.user.is_superuser == True:
                fm = EditadminProfile(instance = request.user)
                users = User.objects.all()
            else:
                fm = EdituserProfile(instance = request.user)
                users = None
        return render(request, 'singIn/profile.html', {'name':request.user.username, 'form':fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')
# logout
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# changepass
def userchange_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data =request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'singIn/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def user_details(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk= id)
        fm = EditadminProfile(instance =pi)
        return render(request, 'singIn/userdetails.html',{"form":fm})
    else:
        HttpResponseRedirect('/login/')

    