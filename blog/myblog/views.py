from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views.generic import View,ListView
from .models import Post, Category,Author
from .forms import UserForm,AuthorForm
import pdb

class Blog_post(View):
	def get(self, request):
		post = Post.objects.all()
		approved_post = Post.objects.filter(status = 'approved')
		pending_post = Post.objects.filter(status = 'pending')

		post_cat = Post.objects.filter(category__name="Feature Post", status = 'approved').latest("date_created")
		# pdb.set_trace()

		context = {
			'allpost' : approved_post,
			'pending' : pending_post,
			'post_cat' : post_cat,
			'post' : post
		}
		return render(request,"index.html", context = context)


	def post(self,request):
		return render(request,"index.html")


class Blog_Details(ListView):
	def get(self, request,pk):
		#post_details = Post.objects.get(pk=pk)
		post_details = get_object_or_404(Post,pk=pk)
		context={
			'post_details':post_details
		}
		return render(request,"details.html",context=context)
	
	def post(self, request,pk):
		#post_details = Post.objects.get(pk=pk)
		post_details = get_object_or_404(Post,pk=pk)
		context={
			'post_details':post_details
		}
		return render(request,"details.html",context=context)
	
class Blog_Category(View):
	def get(self, request, pk):

		cat_post = get_object_or_404(Category,pk=pk)  #values_list('category__name',flat="True")

		context = {
			'cat_post' : cat_post
		}
		return render(request,"categories.html", context = context)


	def post(self,request, pk):

		cat_post = get_object_or_404(Category,pk=pk)

		context = {
			'cat_post' : cat_post
		}
		return render(request,"categories.html", context = context)

class Blog_Login(View):
	def post(self,request,pk):
		user_form = UserForm(request.POST)
		author_form = AuthorForm(request.POST)

		if user_form.is_valid() and author_form.is_valid():
			user_form.save()
			author_form.save()
			return HttpResponseRedirect(request,'index.html')        
	
	def get(self, request):
		return render(request, 'signup.html')
	