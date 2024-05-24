from django.shortcuts import render
from django.http import HttpResponse

# Your existing views might be here...

def home(request):
    return HttpResponse("Welcome to Rentify!")
