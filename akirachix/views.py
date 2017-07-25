from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def welcome(request):
   return render(request,'welcome_akirachix.html')

def students(request):
   students=Student.object.all()
   return HttpResponse("students[0].names")
   
