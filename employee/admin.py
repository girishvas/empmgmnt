from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
	list_display 	= ('code', 'name', 'createdOn')
	list_filter 	= ['createdOn']
	search_fields 	= ['code', 'name']

admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'email', 'department', 'salary', 'mobile', 'createdOn')
	list_filter 	= ['department', 'createdOn']
	search_fields 	= ['code', 'name', 'department']

admin.site.register(Employee, EmployeeAdmin)