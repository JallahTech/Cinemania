from django.db import models
from django.contrib.auth.models import User



class Signup(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = (
		("Male", 'M'),
		("Female", 'F'),
		("Other", 'O')
		)
	user_gender = models.CharField(max_length=15, choices=gender)
	profile_image = models.ImageField(default='icon.jpg', upload_to='profiles')
	

	def __str__(self):
		return self.user.username 


class CreatePost(models.Model):
	owner = models.ForeignKey(Signup, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	movie_date = models.DateField()
	movie_actors = models.TextField()
	description = models.TextField()
	genre = (
		("Romantic", 'Romantic'),
		("Comedy", 'Comedy'),
		("Cartoon", 'Cartoon'),
		("Actions", 'Actions')
		)

	movie_genre = models.CharField(max_length=15, choices=genre)
	movie_poster = models.ImageField(default='icon.jpg', upload_to='movies')
	posted = models.DateTimeField()

	def __str__(self):
		return self.title

class AddComment(models.Model):
	names = models.CharField(max_length=150)
	email = models.EmailField()
	text = models.TextField(max_length=1000)
	added = models.DateTimeField()

	def __str__(self):
		return self.names
			
						
					
