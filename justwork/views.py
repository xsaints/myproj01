from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm


from django.urls import reverse


def home(request):
	#return render(request, '')
	#return HttpResponse('<h2>hello</h2>')
	return render(request, 'home.html', {'name': 'Just Work'})   


def all_departments(request):
	departments= Department.objects.all()
	return render(request, 'all_departments.html', {'name': 'department Tracker', 'departments': departments})	    



def new_department(request):
	form= DepartmentForm()

	if request.method == 'POST':
		form= DepartmentForm(request.POST)
		if form.is_valid():
			#print(request.POST['subject'])
			#print("hello world!")

			#form.save()
			new_department= form.save(commit= False)
			#new_Department.owner= request.user
			new_department.save()

			return HttpResponseRedirect(reverse('justwork:all_departments'))
	return render(request, 'new_department.html', {'form': form})


def all_employees(request):
	employees= Employee.objects.all()
	return render(request, 'all_employees.html', {'name': 'employee Tracker', 'employees': employees})	    

def specific_employee(request, emp_id):
	emp= Employee.objects.get(id= emp_id)

	#if topic.owner != request.user:
	#	raise Http404

	return render(request, 'specific_employee.html', {'emp': emp})	


def new_employee(request):
	form= EmployeeForm()

	if request.method == 'POST':
		form= EmployeeForm(request.POST)
		if form.is_valid():
			#print(request.POST['subject'])
			#print("hello world!")

			#form.save()
			new_employee= form.save(commit= False)
			#new_Department.owner= request.user
			new_employee.save()

			return HttpResponseRedirect(reverse('justwork:all_employees'))
	return render(request, 'new_employee.html', {'form': form})


def edit_employee(request, emp_id):
	employee= Employee.objects.get(id= emp_id)

	#topic_id= employee.topic.id
	#topic= Topic.objects.get(id= topic_id)
	department= employee.department_id

	#if topic.owner != request.user:
	#	raise Http404

	if request.method != 'POST':
		form= EmployeeForm(instance= employee)
	else:
		form= EmployeeForm(instance= employee, data= request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('justwork:specific_employee', args= [employee.id]))

	return render(request, 'edit_employee.html', {'form': form, 'employee': employee, 'department': department})	
    