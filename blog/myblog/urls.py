from django.urls import path
from .views import Blog_post, Blog_Details, Blog_Category,Blog_Login

urlpatterns = [
	path("", Blog_post.as_view(),name = "post"),
    path('details_blog/<int:pk>',Blog_Details.as_view(),name = "details"),
	path('categories/<int:pk>',Blog_Category.as_view(),name = "categories"),
	path('login',Blog_Login.as_view(),name = "login"),

]
