from django import forms


from .models import Department, Employee  #, UsersN
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class DepartmentForm(forms.ModelForm):
    class Meta:
        model= Department
        #fields = '__all__'
        fields= ['department_name', 'manager_id']
        labels= {'department_name': '', 'manager_id': 'Manager',}

        widgets={
        'department_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}),
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
        labels= {'first_name':'', 'hire_date':'', 'department_id':'Department', 'manager_id':'Manager'}
        widgets = {
        'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
        'hire_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':"Hire Date(YYYY-mm-dd)"}),         
        #'department_id': forms.Select,

        }
        
    def clean_hire_date(self):
        data = self.cleaned_data['hire_date']
        
        if data >= datetime.date.today() + datetime.timedelta(30):
            raise ValidationError(_('Hire date is more than a month in the future')) 
            
        if data <= datetime.date(2012,12,31):
            raise ValidationError(_('Hire date should be after 2012'))
            
        return data
        