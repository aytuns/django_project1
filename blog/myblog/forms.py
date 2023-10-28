from django.forms import ModelForm

from .models import Author,User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['profile','user','display_name', 'about']
