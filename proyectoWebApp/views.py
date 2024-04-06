from django.shortcuts import render, HttpResponse


# Create your views here.
# home,servicios,tienda,bloc,contatos


def home(request):
    return render(request,"proyectoWebApp/Home.html")







