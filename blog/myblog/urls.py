from django.urls import path
from .views import Blog_post, Blog_Details

urlpatterns = [
	path("", Blog_post.as_view(),name = "post"),
    path('details_blog/<int:pk>',Blog_Details.as_view(),name = "details")
]
