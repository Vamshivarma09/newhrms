from django.contrib import admin
from .models import *

# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    empdetails = ('first_name', 'last_name','email','phone')

class departmentAdmin(admin.ModelAdmin):
    authority = ('name','employees')

class leaveAdmin(admin.ModelAdmin):
    balanceleave = ('employee','start_date','end_date', 'reason')

admin.site.register(Employee,employeeAdmin),
admin.site.register(Department,departmentAdmin),
admin.site.register(Leave,leaveAdmin),