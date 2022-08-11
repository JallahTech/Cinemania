from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Signup, CreatePost, AddComment
from django.utils import timezone
import datetime
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def welcome(request):
	if request.method == 'POST':
		person_names = request.POST['names']
		person_email = request.POST['email']
		message = request.POST.get('msg')

		new = AddComment(
			
			names = person_names,
			email = person_email,
			text = message,
			added = datetime.datetime.now()
			)
		new.save()
		messages.info(request, 'THANK YOU, YOUR COMMENT WAS SENT!')
	return render(request, "welcome.html")





	return render(request, "welcome.html")

def index(request):
	if request.method == 'POST' and request.FILES:
		f_name = request.POST['firstname']
		l_name = request.POST['lastname']
		email = request.POST['email']
		photo = request.FILES['image']
		password = request.POST['password']
		gender = request.POST['gender']

		user_obj = User(username=email, 
			first_name=f_name, 
			last_name=l_name, 
			email=email, 
			date_joined=datetime.datetime.now()
			)
		user_obj.set_password(password)
		user_obj.save()

		Signup.objects.create(
			user=user_obj,
			user_gender=gender,
			profile_image = photo,
			)
		messages.info(request, 'Accounnt created successfully, Login Here')
		return redirect('index')
	elif request.method == 'POST':
		f_name = request.POST['firstname']
		l_name = request.POST['lastname']
		email = request.POST['email']
		password = request.POST['password']
		gender = request.POST['gender']

		user_obj = User(
			username=email, 
			first_name=f_name, 
			last_name=l_name, 
			email=email, 
			date_joined=datetime.datetime.now()
			)
		user_obj.set_password(password)
		user_obj.save()

		Signup.objects.create(
			user=user_obj,
			user_gender=gender,
			)
		messages.info(request, 'Accounnt created successfully, Login Here')
	return render(request, "Login&Signup.html")

def upload(request):
	if request.method == 'POST' and request.FILES:
		m_title = request.POST['title']
		month = request.POST['month']
		m_actors = request.POST['actors']
		description = request.POST['description']
		m_poster = request.FILES['posters']
		genre = request.POST['genre']

		CreatePost.objects.create(
			owner=request.user.signup,
			title = m_title,
			movie_date = month,
			movie_actors = m_actors,
			description = description,
			movie_genre = genre,
			movie_poster = m_poster,
			posted = datetime.datetime.now()
			)

	return render(request, "movie_form.html")




def User_login(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == 'POST':
			username=request.POST.get('email')
			password=request.POST.get('password')

			login_user=authenticate(request,username=username,password=password)
			if login_user is not None:
				login(request,login_user)
				return redirect("home")
			else:
				messages.info(request,"Username or password is Wrong")

	return render(request,"Login&Signup.html",{})



@login_required(login_url="index")
def home(request):
	movies=CreatePost.objects.all()
	context={'movies':movies}
	return render(request, 'index.html',context)


def Logout_user(request):
	logout(request)
	return redirect('index')

