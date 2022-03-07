from django.shortcuts import render, redirect
from .models import User, Detail
from .user_login_backend import UserBackend
from .pass_match import pass_checks
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
	if request.user.is_authenticated:
		return redirect("index")
	if request.method == "POST":
		password =  request.POST.get("password")
		email = request.POST.get("email")
		user = UserBackend().authenticate(email=email, password=password)
		if user:
			if "remember-me" in request.POST:
				request.session.set_expiry(60*60*24*7)
			else:
				request.session.set_expiry(0)
			login(request, user, backend="users.user_login_backend.UserBackend")
			messages.success(request, f"Welcome To Python Hub {user.first_name}")
			if "next" in request.GET:
				return redirect(request.GET.get("next"))
			else:
				return redirect("index")
		else:
			messages.error(request, "Email or Password is Invalid")
	return render(request, "users/login.html", {"title": "Login"})

def about(request):
	return render(request, "users/about.html", {"title": "About"})

@pass_checks
def signup(request):
	 if request.method == "POST":
	 	if not User.objects.filter(email=request.POST.get("email")).first():
	 		user = User(first_name=request.POST.get("first_name"),
			last_name=request.POST.get("last_name"),
				email=request.POST.get("email"),
				password=request.POST.get("password"))
	 		user.save()
	 		messages.success(request, "Account Created")
	 		user = UserBackend().authenticate(email=request.POST.get("email"),
									password=request.POST.get("password"))
	 		login(request, user, backend="users.user_login_backend.UserBackend")
	 		return redirect("index")
	 	else:
	 		messages.error(request, "Email Already Exists")
	 		return redirect("signup")
	 return render(request, "users/signup.html", {"title": "Sign Up"})

def intro(request):
	if request.user.is_authenticated:
		return redirect("index")
	return render(request, "users/intro.html", {"title": "Welcome User"})

def user_logout(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			logout(request)
			messages.success(request, "Logged Out Successfully")
			return redirect("login")
		return render(request, "users/logout.html", {"title": f"Logout {request.user.first_name}"})

def pass_reset(request):
	if request.method == "POST":
		email = request.POST.get("email")
		user = User.objects.filter(email=email).first()
		if user:
			token = default_token_generator.make_token(user)
			url = f"http://127.0.0.1:8000/password-reset-confirm/?token={token}&email={email}"
			msg = f"This is your password reset mail for {user.first_name} {user.last_name}. Please click on the link below to change your password\n{url}"
			send_mail("Password Reset Mail | Python Hub", msg, "arijid79@gmail.com",
						[email])

			messages.info(request, "An email has been sent containing instructions for resetting your password")
			return redirect("login")
		else:
			messages.error(request, "Email Already Exists")
			return redirect("pass-reset")
	return render(request, "users/password-reset.html", {"title": "Request Password Reset"})

@pass_checks
def pass_confirm(request):
	token = request.GET.get("token")
	email = request.GET.get("email")
	user = User.objects.filter(email=email).first()

	if request.method == "POST":
		password = request.POST.get("password")
		confirm_password = request.POST.get("confirm-password")

		update_pass_user = User.objects.filter(email=email).first()
		update_pass_user.password = password
		update_pass_user.save()
		messages.success(request, "Password Changed Successfully")
		return redirect("login")
	if default_token_generator.check_token(user, token):
		return render(request, "users/password.html", {"title": "Password Reset"})
	return render(request, "users/password.html", {"title": "Password Reset"})

@login_required
def profile(request):
	user = request.user
	if request.method == "POST":
		user = User.objects.filter(id=user.id)
		first_name = request.POST.get("first-name")
		last_name = request.POST.get("last-name")
		email = request.POST.get("email")
		pinfo = request.POST.get("pinfo")
		user.update(first_name=first_name, last_name=last_name, email=email)
		messages.success(request, f"Profile Intformation Updated Successfully")
		Detail.objects.filter(user=user.first()).update(personal_info=pinfo)
		return redirect("profile")
	return render(request, "users/profile.html", {"title": f"{request.user.first_name} {request.user.last_name} Profile"})
