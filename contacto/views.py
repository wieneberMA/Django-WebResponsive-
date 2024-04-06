from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            email = EmailMessage("Mensaje desde Gestion de Pedidos",
            "El Ususario con Nombre {} Con Direccion {} Escribe lo Siguiente:\n\n {}".format(nombre,email,mensaje),"",["wieneber76@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    return render(request, "contacto/Contacto.html", {'miFormulario': formulario_contacto})