from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    html = f"""
        <h1>Home Page</h1>
    """
    return HttpResponse(html)
