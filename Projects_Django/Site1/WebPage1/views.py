from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<center><h1><font color=red><br><br><br>Hello World from Python DJANGO!!!</font></h1></center>")

