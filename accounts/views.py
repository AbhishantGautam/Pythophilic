from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
import uuid
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_verify(request, auth_token):
    profile_obj =  Profile.objects.filter(auth_token=auth_token)
    if profile_obj:
        profile_obj.update(is_verified = True)
        return render(request,"accounts/success.html")
    else:
        return redirect("/error")

def show_accounts(request):
    if request.method == "POST":
        username_ = request.POST.get("username")
        password_ = request.POST.get("password")

        user_obj =  User.objects.filter(username = username_)
        if user_obj is None:
            return redirect("/accounts")
        print(user_obj)
        profile_obj = Profile.objects.get(user__in=user_obj)
        print(profile_obj)
        if not profile_obj.is_verified:
            return redirect("/accounts")
        user = authenticate(username=username_,password=password_)
        if user is None:
            return redirect("/accounts")
        login(request,user)
        return redirect("/")
    return render(request, "accounts/accounts.html")

def show_register(request):
    if request.method == "POST":
        username_ = request.POST.get("username")
        email_ = request.POST.get("email")
        password_ = request.POST.get("password")
        try:
            if User.objects.filter(username=username_):
                messages.success(request, "Username already registered")
            if User.objects.filter(email=email_):
                messages.success(request, "Email is already registered")
            user_obj = User.objects.create(username=username_, email=email_)
            user_obj.set_password(password_)
            user_obj.save()
            auth_token_ = str(uuid.uuid4())
            profile_obj = Profile(user = user_obj, auth_token=auth_token_)
            profile_obj.save()
            send_mail_after_reg(email_,auth_token_)
            return render(request, "accounts/token_send.html")
        except Exception as e:
            print(e)
    return render(request, "accounts/register.html")
        
def show_success(request):
    return render(request, "accounts/success.html")

def token_send(request):
    return render(request, "accounts/token_send.html")

def send_mail_after_reg(email,token):
    subject = "your account needs to be verified"
    message = f"paste the link to verify: http://127.0.0.1:8000/accounts/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

def show_logout(request):
    auth.logout(request)
    return redirect("/")