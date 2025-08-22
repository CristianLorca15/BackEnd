from django.http import HttpResponse

def inicio(request):
    nombre = "Cristian Lorca"
    return HttpResponse( f"¡Bienvenidos a mi primera app Django, {nombre}!")
