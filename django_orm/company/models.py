from django.db import models
from django.contrib.auth.models import User

class Profile(User):
	user_name = User.username
	email_add = User.email
	passwd = User.password

	def __str__(self):
		return self.user_name

class Department(models.Model):
	DEPS = [('ADMIN','ADMIN DEPARTMENT'),
	 		('IT','IT DEPARTMENT'),
			('ACCOUNTS','ACCOUNT DEPARTMENT'),
			('HR','HR DEPARTMENT'),
			('SALES','SALES DEPARTMENT')]

	dep_name = models.CharField(max_length=20,choices=DEPS,unique=True)

	class Meta:
		ordering = ['dep_name']

	def __str__(self):
		return self.dep_name

class Branches(models.Model):
	Brnch = [('LAGOS','LAGOS BRANCH'),
	  		('IBADAN','IBADAN BRANCH'),
			('PH','PH BRANCH'),
			('ABUJA','ABUJA BRANCH'),
			('ENUGU','ENUGU BRANCH')]

	branch_name = models.CharField(max_length=20,choices=Brnch,unique=True)

	class Meta:
		ordering = ['branch_name']

	def __str__(self):
		return f'{self.branch_name}'


class branch_dept(models.Model):
	branch = models.ForeignKey(Branches,on_delete=models.CASCADE,null=False)
	dept = models.ForeignKey(Department,on_delete=models.CASCADE,null=False)

	class Meta:
		ordering = ['branch']

	def __str__(self):
		return f'{self.branch} - {self.dept}'


class Employee(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	salary = models.IntegerField()
	dob = models.DateField()
	user_name = models.OneToOneField(Profile, on_delete=models.CASCADE,null=True)
	location = models.ForeignKey(branch_dept,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
