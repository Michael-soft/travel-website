import email
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):            #if someone want to signup on our site
    if request.method=='POST':
        uname = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['initial']
        password2 = request.POST['confirm']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is used by another user')
                return redirect('accounts:signup')
            else:
                user = User.objects.create_user(username=uname,email=email,first_name=firstname,last_name=lastname,password=password2)  # type: ignore
                user.save()  
                messages.success(request,'User creation Succeed!')
                return redirect('accounts:signin')
        else:
            messages.warning(request,"password not matched")
            return redirect('accounts:signup')
    else:
        return render(request,'accounts/signup.html')
    


def signin(request):
    if request.method=="POST":             #if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None: 
            login(request,user)
            username = user.username
            messages.success(request,"You are successfully logged in") #routes to 'home' on successful login  
            return render(request,'accounts/landing-page-after-sign-in.html',{'username': username})
        
        else: 
            messages.error(request,"Invalid username or password")
            return redirect('accounts:signin')                                #re routes to login page upon unsucessful login
        
    else: 
            return render(request,'accounts/signIn.html')
        
def passwordupdate (request):
 if request.method=='POST':
    password1 = request.POST['initial']
    password2 = request.POST['confirm']
    username = request.POST['username']
    if password1==password2:
        u=User.objects.get(username=username)
        print(u.email)
        u.set_password(password2)
        u.save()
        return redirect('accounts:signin') 
    else:
        messages.error(request,"password mismatch")
        return redirect('accounts:passwordrecovery') 
 return render(request, "accounts/passwordupdate.html") 

def passwordrecovery(request):
    if request.method=='POST':
        #  email = request.POST['email']
         email=request.POST.get('email')
         if email is not None:
            if User.objects.filter(email=email).exists():
             emails = User.objects.get(email=email)
             return render(request,"accounts/passwordupdate.html", context={'email':emails})
         else: 
             messages.warning(request,('Invalid Email Address'))
             return redirect('accounts:signin')
    
    return render(request, "accounts/PasswordRecovery.html")

def terms(request):
    return render(request, "accounts/terms-and-policies.html")

def serviceterms(request):
    return render(request, "accounts/terms-of-service.html")


def termsup(request):
    return render(request, "accounts/terms-and-policies-signup.html")


def landing(request):
    return render(request, "accounts/landing-page-after-sign-in.html") 

def myaccount(request):
        return render(request, "accounts/my-account.html")