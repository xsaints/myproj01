from django import forms

from .models import Department, Employee  #, UsersN


class DepartmentForm(forms.ModelForm):
    class Meta:
        model= Department
        #fields = '__all__'
        fields= ['department_id', 'department_name', 'manager_id', 'location_id']
        labels= {'department_id': '', 'department_name': '', 'manager_id': '', 'location_id': '',}

        widgets={
        'department_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department ID'}),
        'department_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}),
        'manager_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager ID'}),        
        'location_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location ID'}),        
        }


class EmployeeForm(forms.ModelForm):
	class Meta:
		model= Employee
		exclude= ['entry_date', 'last_update']
		widgets = {'department_id': forms.Select,}
