from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate #Para login_request
from django.contrib.auth.forms import AuthenticationForm #Para login_request

from django.shortcuts import redirect #Para register_request
from .forms import NewUserForm #Para register_request
from django.contrib import messages #Para register_request

from django.contrib.auth import logout #Para logout

def index(request):
    return render(request,'frontend/templates/frontend/index.html')

def register_request(request):
	"Para registro dos usuários do site"
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			#messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	"Para login dos usuários do site"
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
    """Logout de usuários do site"""
    logout(request) 
    return redirect("/")


def password_reset_request(request):
	from django.shortcuts import render, redirect
	from django.core.mail import send_mail, BadHeaderError
	from django.http import HttpResponse
	from django.contrib.auth.forms import PasswordResetForm
	from django.contrib.auth.models import User
	from django.template.loader import render_to_string
	from django.db.models.query_utils import Q
	from django.utils.http import urlsafe_base64_encode
	from django.contrib.auth.tokens import default_token_generator
	from django.utils.encoding import force_bytes

	if request.method == "POST":
			password_reset_form = PasswordResetForm(request.POST)
			if password_reset_form.is_valid():
					data = password_reset_form.cleaned_data['email']
					associated_users = User.objects.filter(Q(email=data))
					if associated_users.exists():
							for user in associated_users:
									subject = "Password Reset Requested"
									email_template_name = "password/password_reset_email.txt"
									c = {
									"email":user.email,
									'domain':'127.0.0.1:8000',
									'site_name': 'Website',
									"uid": urlsafe_base64_encode(force_bytes(user.pk)),
									"user": user,
									'token': default_token_generator.make_token(user),
									'protocol': 'http',
									}
									email = render_to_string(email_template_name, c)
									try:
											send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
									except BadHeaderError:
											return HttpResponse('Invalid header found.')
									return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

    

    
