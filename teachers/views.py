from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def django_instructors(request):
    i=5
    return HttpResponse(f'Number of instructors for course: {i}')