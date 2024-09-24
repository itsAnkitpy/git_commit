from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileUpdateForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from .models import *
from dating_app.models import Message

# Create your views here.


def register(req):
    if req.method == "POST":
        Form = UserRegisterForm(req.POST)
        if Form.is_valid():
            Form.save()
            username = Form.cleaned_data.get("username")
            messages.success(req, f"Account Created. You can now log in")
            return redirect("login")
    else:
        Form = UserRegisterForm()
    return render(req, "users/register.html", {'form': Form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("date-page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

@login_required
def profile(req):
    user = req.user
    profile = Profile.objects.get(user=user)
    likes = user.likes.all()  # Fetch users who have liked the current user
    unreadMessages = Message.objects.filter(
        receiver=req.user).filter(status=False).count()
    if req.method == "POST":
        form = ProfileUpdateForm(
            req.POST, req.FILES, instance=req.user.profile)

        if form.is_valid():
            form.save()
            messages.success(req, "Account Updated")
            return redirect("profile-page")
    else:
        form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'form': form,
        'likes': likes,
        'unreadmsgs': unreadMessages
    }

    return render(req, "users/profile.html", context)
