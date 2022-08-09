from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm


from django.urls import reverse


def index(request):
	#return render(request, '')
	#return HttpResponse('<h2>hello</h2>')
	return render(request, 'index.html', {'name': 'Just Work'})   


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