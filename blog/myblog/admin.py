from django.contrib import admin
from .models import *

@admin.register(Post)

class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'date_created', 'updated_on', 'author','category','status')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('display_name','user','profile')