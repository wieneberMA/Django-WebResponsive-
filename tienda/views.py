from django.shortcuts import render
from .models import Producto,CategoriasProdructos
# Create your views here.

def tienda(request):
    productos=Producto.objects.all()


    return render(request,"tienda/Tienda.html",{'productos':productos})