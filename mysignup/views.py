from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import SignupForm,EditUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
#views for signup page 
def sign_up_view(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            #messages.success is predefine method
            messages.success(request,'account created successfully')
            fm.save()
    else:
            fm=SignupForm()
    return render(request,'signup_page.html',{'form':fm})
# we are create here views for login page
def login_page_view(request):
    if request.method=="POST":
        # predfine AuthenticationForm import above
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #predfine authenticate method as import above
            user=authenticate(username=uname,password=upass)
            if user is not None:
            #predefine login method import above
                login(request,user)
                #pedefine messages method import above
                messages.success(request,"login successfully")
                return HttpResponseRedirect("/profile/")
    else:
        fm=AuthenticationForm()
    return render(request,'login_page.html',{'form':fm})

def profile_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm=EditUserProfile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"profileupdeted successfully")
                return HttpResponseRedirect('/profile/')
        else:
            fm=EditUserProfile(instance=request.user)
        return render(request,'profile_page.html',{'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')
def logout_view(request):
    logout(request)    
    return HttpResponseRedirect('/login/')

def password_change_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password change successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(request.user)
        return render(request,'changepass_page.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

def password_set_view(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password set successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(request.user)
        return render(request,'setpass_page.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")
