from django.urls import path
from . import views

app_name= 'justwork'

urlpatterns = [
	path('', views.index, name = 'index'),

	# add a new department
	path('new_department/', views.new_department, name= 'new_department'),
    
	# list all departments
	path('all_departments/', views.all_departments, name= 'all_departments'),

	# add a new employee
	path('new_employee/', views.new_employee, name= 'new_employee'),
    
	# list all employees
	path('all_employees/', views.all_employees, name= 'all_employees'),

    
]    