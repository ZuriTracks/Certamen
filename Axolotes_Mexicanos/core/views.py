from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def historia(request):
    return render (request,"core/historia.html")

def contactos(request):
    return render(request, 'core/Contactos.html')

def albums(request):
    return render(request, 'core/albums.html')
