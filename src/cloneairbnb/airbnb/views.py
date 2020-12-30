from django.shortcuts import render
from .models import Cliente

def login(req):
    return render(req, 'airbnb/index.html')
