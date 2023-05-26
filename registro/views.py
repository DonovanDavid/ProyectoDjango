from django.http import HttpResponse, JsonResponse
from .models import Ciudad,Persona,tipoDocumento
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
def consultaPersona(request):
    if request.method == 'GET':
        tipoDocumentos = tipoDocumento.objects.all()
        ciudades = Ciudad.objects.all()
        personas = Persona.objects.all()
        return render(request, 'Personas.html', {
            'tipoDocumentos' : tipoDocumentos,
            'ciudad' : ciudades,
            'persona' : personas
        })
    else:
        print("creando")
        tipo_documento = get_object_or_404(tipoDocumento, id=request.POST['tipoDocumento'])
        lugar_Residencia = get_object_or_404(Ciudad, id=request.POST['lugarResidencia'])
        Persona.objects.create(id=request.POST['id'], nombres=request.POST['nombres'], apellidos=request.POST['apellidos'],tipoDocumento=tipo_documento, documento=request.POST['documento'], lugarResidencia=lugar_Residencia, fechaNacimiento=request.POST['fechaNacimiento'], email=request.POST['email'], telefono=request.POST['telefono'], usuario=request.POST['usuario'], password=request.POST['password'])
        return redirect('/personas')

def eliminarPersona(request, id):
    obj = Persona.objects.get(pk = id)
    print("Estoy eliminando")
    obj.delete()
    tipoDocumentos = tipoDocumento.objects.all()
    ciudades = Ciudad.objects.all()
    personas = Persona.objects.all()
    return render(request, 'Personas.html', {
            'tipoDocumentos' : tipoDocumentos,
            'ciudad' : ciudades,
            'persona' : personas
        })

def consultaTipoDocumento(request):
    if request.method == 'GET':
        tipoDocumentos = tipoDocumento.objects.all()
        return render(request, 'tipoDocumento.html', {
            'tipoDocumento' : tipoDocumentos
        })
    else:
        tipoDocumento.objects.create(id=request.POST['id'], nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
        return redirect('/tipoDocumento')

def consultaCiudades(request):
    #ciudades = list(Ciudad.objects.values())
    if request.method == 'GET':
        ciudades = Ciudad.objects.all()
        return render(request, 'Ciudades.html', {
            'Ciudades' : ciudades
        })
    else:
        Ciudad.objects.create(id=request.POST['id'], nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
        return redirect('/ciudades') 
    
def consultaCiudad(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    return HttpResponse("Ciudad = %s" %ciudad.nombre)