from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status , generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from .models import *
from .serializers import *
import coreapi
from rest_framework.schemas import AutoSchema

class DptViewSchema(AutoSchema):
	def get_manual_fields(self, path, method):
		extra_fields 		= []
		if method.lower() in ['post', 'put']:
			extra_fields 	= [
				coreapi.Field('name')
			]
		manual_fields 		= super().get_manual_fields(path, method)
		return manual_fields + extra_fields


class EmpViewSchema(AutoSchema):
	def get_manual_fields(self, path, method):
		extra_fields 		= []
		if method.lower() in ['post', 'put']:
			extra_fields 	= [
				coreapi.Field('name'),
				coreapi.Field('email'),
				coreapi.Field('mobile'),
				coreapi.Field('salary'),
				coreapi.Field('department'),
			]
		manual_fields 		= super().get_manual_fields(path, method)
		return manual_fields + extra_fields


class SearchSchema(AutoSchema):
	def get_manual_fields(self, path, method):
		extra_fields 		= []
		if method.lower() in ['get']:
			extra_fields 	= [
				coreapi.Field('department'),
				coreapi.Field('min_salary'),
				coreapi.Field('max_salary'),
			]
		manual_fields 		= super().get_manual_fields(path, method)
		return manual_fields + extra_fields


@permission_classes((AllowAny, ))
class DptListView(generics.GenericAPIView):
	serializer_class 		= DepartmentSerializer
	schema 					= DptViewSchema()

	def get(self, request):
		emp_det 			= Department.objects.all()
		serializer 			= DepartmentSerializer(emp_det, many=True)
		return Response({"dpt_details": serializer.data})

	def post(self, request):
		emp_det 			= request.data
		serializer 			= DepartmentSerializer(data=emp_det)
		if serializer.is_valid(raise_exception=True):
			dpt_det_saved	= serializer.save()
			return Response({"success": "Department is '{}' created successfully".format(dpt_det_saved.name)}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny, ))
class DptDetailView(APIView):
	serializer_class 		= DepartmentSerializer
	schema 					= DptViewSchema()

	def get(self, request, slug):
		dpt_det 			= get_object_or_404(Department.objects.all(), code=slug)
		serializer 			= DepartmentSerializer(dpt_det, many=False)
		return Response({"dpt_details": serializer.data})

	def put(self, request, slug):
		saved_dpt_det 		= get_object_or_404(Department.objects.all(), code=slug)
		data = request.data
		serializer 			= DepartmentSerializer(instance=saved_dpt_det, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			emp_det_saved 	= serializer.save()
		return Response({"success": "Department '{}' updated successfully".format(saved_dpt_det.name)})

	def delete(self, request, slug):
		emp_det 			= get_object_or_404(Department.objects.all(), code=slug)
		emp_det.delete()
		return Response({"message": "Department with Name `{}` has been deleted.".format(emp_det)},status=204)


@permission_classes((AllowAny, ))
class EmpListView(APIView):
	serializer_class 		= EmployeeSerializer
	schema 					= EmpViewSchema()

	def get(self, request):
		emp_det 			= Employee.objects.all()
		serializer 			= EmployeeDisplaySerializer(emp_det, many=True)
		return Response({"emp_details": serializer.data})

	def post(self, request):
		emp_det 			= request.data
		serializer 			= EmployeeSerializer(data=emp_det)
		if serializer.is_valid(raise_exception=True):
			emp_det_saved	= serializer.save()
			return Response({"success": "Employee is '{}' created successfully".format(emp_det_saved.name)}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny, ))
class EmpDetailView(APIView):
	serializer_class 		= EmployeeSerializer
	schema 					= EmpViewSchema()
	def get(self, request, pk):
		emp_details 		= get_object_or_404(Employee.objects.all(), pk=pk)
		serializer 			= EmployeeSerializer(emp_details, many=False)
		return Response({"emp_details": serializer.data})

	def put(self, request, pk):
		saved_emp_det 		= get_object_or_404(Employee.objects.all(), pk=pk)
		data = request.data
		serializer 			= EmployeeSerializer(instance=saved_emp_det, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			emp_det_saved 	= serializer.save()
		return Response({"success": "Employee '{}' updated successfully".format(emp_det_saved.name)})

	def delete(self, request, pk):
		emp_det 			= get_object_or_404(Employee.objects.all(), pk=pk)
		emp_det.delete()
		return Response({"message": "Employee with Name `{}` and id `{}` has been deleted.".format(emp_det, pk)},status=204)


@permission_classes((AllowAny, ))
class EmpSearchView(APIView):
	serializer_class 		= EmployeeSerializer
	# schema 					= SearchSchema()
	def get(self, request):
		emp_det 			= Employee.objects.all()
		print(request.data)

		try:
			dpt 			= request.data.get('department')
			emp_det 		= emp_det.filter(department__name__lower=dpt.lower())
		except:
			pass

		try:
			sal_max 		= request.data.get('maximum_salary')
			emp_det 		= emp_det.filter(salary__lte=sal_max)
		except:
			pass

		try:
			min_sal 		= request.data.get('minumum_salary')
			emp_det 		= emp_det.filter(salary__gte=min_sal)
		except:
			pass

		serializer 			= EmployeeDisplaySerializer(emp_det, many=True)
		return Response({"emp_details": serializer.data})