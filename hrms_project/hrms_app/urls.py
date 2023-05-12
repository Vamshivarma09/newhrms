from django.urls import path
from .views import *

urlpatterns = [
    
    path('employees', employee_list),
    
    
]