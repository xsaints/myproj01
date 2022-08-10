from django.urls import path
from . import views

app_name= 'justwork'

urlpatterns = [
    path('', views.home, name = 'home'),

	# add a new department
    path('new_department/', views.new_department, name= 'new_department'),
    
	# list all departments
    path('all_departments/', views.all_departments, name= 'all_departments'),

	# add a new employee
    path('new_employee/', views.new_employee, name= 'new_employee'),
    
	# list all employees
    path('all_employees/', views.all_employees, name= 'all_employees'),

	# list specific employee
    path('specific_employee/(<emp_id>)/', views.specific_employee, name= 'specific_employee'),
    
    # edit an entry
    path('edit_employee/(<emp_id>)/', views.edit_employee, name= 'edit_employee'), 
]    