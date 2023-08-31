from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Author(models.Model):
	profile = models.ImageField(upload_to='image')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=50)

	def __str__(self):
		return self.display_name
	

post_status = (
	('pending','pending'),
	('delete','delete'),
	('approved','approved')
)

class Post(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField(max_length=1000)
	upload_image = models.ImageField(upload_to = 'blog')
	date_created = models.DateField(auto_now_add = True)
	updated_on = models.DateField(auto_now = True)
	status = models.CharField(choices = post_status, default='pending',max_length=50)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title