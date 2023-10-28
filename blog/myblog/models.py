from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Author(models.Model):
	profile = models.ImageField(upload_to='media/authors/')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	display_name = models.CharField(max_length=50)
	about = models.TextField(max_length=500,default="I AM AN AUTHOR")

	def __str__(self):
		return self.display_name
	

post_status = (
	('pending','pending'),
	('delete','delete'),
	('approved','approved')
)

class Post(models.Model):
	title = models.CharField(max_length=300)
	body = models.TextField(max_length=10000)
	upload_image = models.ImageField(upload_to = 'media/posts/')
	date_created = models.DateField(auto_now_add = True)
	updated_on = models.DateField(auto_now = True)
	status = models.CharField(choices = post_status, default='pending',max_length=50)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Comments(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_body = models.TextField(max_length=400)
	commenter_name = models.CharField(max_length=300)
	date_created = models.DateTimeField(auto_now_add=False)
	user = models.ForeignKey(Author, on_delete=models.CASCADE, default = "comments")

	def __str__(self):
		return self.comment_body
