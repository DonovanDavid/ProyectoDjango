from django.contrib import admin
from .models import Ciudad
from .models import tipoDocumento
from .models import Persona

admin.site.register(Persona)
admin.site.register(Ciudad)
admin.site.register(tipoDocumento)

# Register your models here.
