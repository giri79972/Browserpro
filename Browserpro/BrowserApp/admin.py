from django.contrib import admin
from .models import Employee
# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    list_display = ['first_name','last_name','company','email','sal','loc']
admin.site.register(Employee,AdminEmployee)