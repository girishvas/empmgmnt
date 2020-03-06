from django.urls import path
from .views import *


urlpatterns = [
	path('dptlist/', DptListView.as_view()),
	path('dptdetails/<slug:slug>', DptDetailView.as_view()),
	path('emplist/', EmpListView.as_view()),
	path('empdetails/<int:pk>', EmpDetailView.as_view()),
	path('empsearch/', EmpSearchView.as_view()),
]