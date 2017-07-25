from django.contrib import admin

# Register your models here.
from akirachix.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['names']


admin.site.register(Student,StudentAdmin)



