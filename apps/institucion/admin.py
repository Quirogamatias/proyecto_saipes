from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class RespuestaInline(admin.StackedInline):
    model = Respuesta
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    inline = [RespuestaInline]
    list_display = ('asunto', 'fecha_publicacion', 'publicado_hoy')
    #list_filter = ('fecha_publicacion')

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno

class AlumnoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['apellido']
    list_display = ('dni','nombre','apellido','email','domicilio','telefono','estado','fecha_de_creacion','id_usuario','notificacion')
    resources_class = AlumnoResource

class ProfesorResource(resources.ModelResource):
    class Meta:
        model = Profesor

class ProfesorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['apellido']
    list_display = ('dni','nombre','apellido','email','domicilio','telefono','estado','fecha_de_creacion','id_usuario','notificacion')
    resources_class = ProfesorResource

class AdministradorResource(resources.ModelResource):
    class Meta:
        model = Administrador

class AdministradorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['apellido']
    list_display = ('nombre','apellido','email','domicilio','telefono','estado','fecha_de_creacion','id_usuario','notificacion')
    resources_class = AdministradorResource

class InscripcionResource(resources.ModelResource):
    class Meta:
        model = Inscripcion

class InscripcionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_inscripcion']
    list_display = ('fecha_inscripcion','id_alumno','id_materia','estado')
    resources_class = InscripcionResource

class CarreraResource(resources.ModelResource):
    class Meta:
        model = Carrera

class CarreraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['carrera']
    list_display = ('carrera','estado')
    resources_class = CarreraResource

class MateriaResource(resources.ModelResource):
    class Meta:
        model = Materia

class MateriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['materia']
    list_display = ('materia','estado')
    resources_class = MateriaResource

class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso

class CursoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','capacidad','turno','estado')
    resources_class = CursoResource

class HorarioResource(resources.ModelResource):
    class Meta:
        model = Horario

class HorarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['dia']
    list_display = ('dia','hora_inicio','hora_fin','id_curso','activo','estado')
    resources_class = HorarioResource

class NotasResource(resources.ModelResource):
    class Meta:
        model = Notas

class NotasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_notas']
    list_display = ('notas','id_materia','id_alumno','tipo','estado')
    resources_class = NotasResource

class AsistenciaResource(resources.ModelResource):
    class Meta:
        model = Asistencia

class AsistenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_asistencia']
    list_display = ('id_materia','id_alumno','dia','asistencia','estado')
    resources_class = AsistenciaResource

class FechaResource(resources.ModelResource):
    class Meta:
        model = Fecha

class FechaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['evento']
    list_display = ('fecha_evento','tipo_evento','evento','estado','fecha_de_creacion')
    resources_class = FechaResource

class PromedioAsistenciaResource(resources.ModelResource):
    class Meta:
        model = Administrador

class PromedioAsistenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_promedioasistencia']
    list_display = ('id_materia','id_alumno','promedio','dias','dias_p','total_d','estado')
    resources_class = PromedioAsistenciaResource

class PromedioNotasFinalResource(resources.ModelResource):
    class Meta:
        model = PromedioNotasFinal

class PromedioNotasFinalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_promedionotasfinal']
    list_display = ('id_materia','id_alumno','cantidad','suma','total','estado')
    resources_class = PromedioNotasFinalResource

class PromedioNotasParcialResource(resources.ModelResource):
    class Meta:
        model = PromedioNotasParcial

class PromedioNotasParcialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_promedionotasparcial']
    list_display = ('id_materia','id_alumno','cantidad','suma','total','estado')
    resources_class = PromedioNotasParcialResource

class InscripcionProfesorResource(resources.ModelResource):
    class Meta:
        model = InscripcionProfesor

class InscripcionProfesorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_inscripcionProfesor']
    list_display = ('fecha_inscripcion','id_profesor','id_materia','estado')
    resources_class = InscripcionProfesorResource

class InscripcionExamenResource(resources.ModelResource):
    class Meta:
        model = InscripcionExamen

class InscripcionExamenAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_inscripcionexamen']
    list_display = ('id_materia','id_alumno','fecha','estado')
    resources_class = InscripcionExamenResource

class RespuestaResource(resources.ModelResource):
    class Meta:
        model = Respuesta

class RespuestaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_respuesta']
    list_display = ('id_pregunta','id_usuario','contenido','mejor_respuesta')
    resources_class = RespuestaResource

class PromedioNotasTotalResource(resources.ModelResource):
    class Meta:
        model = PromedioNotasTotal

class PromedioNotasTotalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id_promedionotastotal']
    list_display = ('id_alumno','cantidad','suma','total','estado')
    resources_class = PromedioNotasTotalResource

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Administrador,AdministradorAdmin)
admin.site.register(Inscripcion,InscripcionAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Materia,MateriaAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Horario,HorarioAdmin)
admin.site.register(Notas,NotasAdmin)
admin.site.register(Asistencia,AsistenciaAdmin)
admin.site.register(Fecha,FechaAdmin)
admin.site.register(PromedioAsistencia,PromedioAsistenciaAdmin)
admin.site.register(PromedioNotasFinal,PromedioNotasFinalAdmin)
admin.site.register(PromedioNotasParcial,PromedioNotasParcialAdmin)
admin.site.register(InscripcionProfesor,InscripcionProfesorAdmin)
admin.site.register(InscripcionExamen,InscripcionExamenAdmin)
admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Respuesta,RespuestaAdmin)
admin.site.register(PromedioNotasTotal)