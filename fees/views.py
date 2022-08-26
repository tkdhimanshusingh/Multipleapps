from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def fees_django(request):
    a=12
    return HttpResponse(f'Course fees is {a}')