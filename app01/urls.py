from django.urls import path
from . import views

app_name= 'app01'

urlpatterns = [
	#path('', views.index, name = 'index'),
    
	# list all expenses
	path('', views.all_expenses, name= 'all_expenses'),
    
]    