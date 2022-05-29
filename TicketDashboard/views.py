from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    HttpResponse("this is main page for the ticket dashboard")