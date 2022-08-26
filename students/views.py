from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def django_students(request):
    s=100
    return HttpResponse(f'Studens Enrolled are: {s}')