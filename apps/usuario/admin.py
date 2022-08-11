from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apps.usuario.models import Usuario,Rol

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['username']
    list_display = ('username','email','nombre','apellido','tipo','imagen','is_active','is_staff')
    resources_class = UsuarioResource

#admin.site.register(Rol)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)
