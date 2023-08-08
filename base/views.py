from django.shortcuts import render

def home(request):
    return render(request, "base/home.html")

def comenza(request):
    return render(request, "base/comenza.html")