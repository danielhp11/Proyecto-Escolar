from django.contrib import admin
from .models import CitaRapida,Producto

# Register your models here.
admin.site.register( CitaRapida )
admin.site.register( Producto )

#configurar titulo de panel
admin.site.site_header="Administrador de Estetica Palagot"
admin.site.index_title="Administrador"
