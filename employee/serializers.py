from rest_framework import serializers
from .models import *


class DepartmentDisplaySerializer(serializers.ModelSerializer):
	class Meta:
		model 		= Department
		fields 		= ('code', 'name')


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model 		= Department
		fields 		= ('code', 'name')

	def create(self, validated_data):
		department 	= Department.objects.create(**validated_data)
		department.save()
		
		return department


class EmployeeDisplaySerializer(serializers.ModelSerializer):
	department_name = serializers.CharField(source='department.name', read_only=False)
	
	class Meta:
		model 		= Employee
		fields 		= ['pk', 'name', 'email', 'mobile', 'salary', 'department_name']


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model 		= Employee
		fields 		= ['pk', 'name', 'email', 'mobile', 'salary', 'department']

	def create(self, validated_data):
		employee 	= Employee.objects.create(**validated_data)
		employee.save()
		
		return employee