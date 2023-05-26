from django.db import models

# Create your models here.

#Tabla tipoDocumento
class tipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=150)
    
    def __str__(self):
        return self.nombre

#Tabla Ciudad
class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre

#Tabla Persona
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    documento = models.IntegerField(max_length=15)
    lugarResidencia= models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechaNacimiento = models.DateField()
    email= models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=10)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



    
