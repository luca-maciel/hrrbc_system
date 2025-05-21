from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    
def pac_ativos(request):
    if request.method == "GET":
        return render(request, "pac_ativos.html")