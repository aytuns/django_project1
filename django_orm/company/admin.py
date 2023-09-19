from django.contrib import admin
from .models import Profile, Department,Branches, Employee, branch_dept

@admin.register(Profile)
class user_profile(admin.ModelAdmin):
	list_display = ('user_name','email_add')


@admin.register(Department)
class user_department(admin.ModelAdmin):
	list_display = ('dep_name',)


@admin.register(Branches)
class user_branch(admin.ModelAdmin):
	list_display = ('branch_name',)


@admin.register(Employee)
class user_branch(admin.ModelAdmin):
	list_display = ('first_name','last_name','dob','location')

@admin.register(branch_dept)
class user_branch(admin.ModelAdmin):
	list_display = ('branch','dept')

