from django import forms

from .models import Department, Employee  #, UsersN


class DepartmentForm(forms.ModelForm):
    class Meta:
        model= Department
        #fields = '__all__'
        fields= ['department_name', 'manager_id']
        labels= {'department_name': '', 'manager_id': '',}

        widgets={
        #'department_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department ID'}),
        'department_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}),
        'manager_id': forms.Select,  #forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager ID'}),        
        #'location_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location ID'}),        
        }

'''
	class Meta:
        model= Employee
        exclude= ['entry_date', 'last_update']
        labels= {'first_name':'', 'hire_date':'', 'department_id':'', 'manager_id':''}
        widgets = {'department_id': forms.Select,
            'hire_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Hire Date'}), 
        }
'''
class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        exclude= ['entry_date', 'last_update']
        labels= {'first_name':'', 'hire_date':'', 'department_id':'', 'manager_id':''}
        widgets = {'department_id': forms.Select,
        'hire_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Hire Date'}), 
        }