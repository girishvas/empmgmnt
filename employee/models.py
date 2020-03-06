from django.db import models


class Department(models.Model):
	code 		= models.CharField(max_length=4, primary_key=True)
	name 		= models.CharField(max_length=30, blank=False, unique=True)

	createdOn 	= models.DateTimeField(auto_now_add=True)
	updatedOn 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Employee(models.Model):
	name 		= models.CharField(max_length=255, blank=False, unique=True)
	email 		= models.EmailField(blank=False, unique=True)
	salary 		= models.IntegerField()
	mobile 		= models.CharField(max_length=12, blank=False, unique=True)
	department 	= models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
	
	createdOn 	= models.DateTimeField(auto_now_add=True)
	updatedOn 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('createdOn',)