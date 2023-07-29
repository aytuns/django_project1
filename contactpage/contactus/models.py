from django.db import models

# Create your models here.

class ContactInfo(models.Model):
	fullname = models.CharField(max_length=100)
	phone =   models.CharField(max_length=20)
	email =   models.EmailField(max_length=300)
	message   =  models.TextField(max_length=1000)
	location =  models.CharField(max_length=30)
	subject = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.fullname} created on {self.created.replace(microsecond=0)}"

	class Meta:
		ordering = ['-created']