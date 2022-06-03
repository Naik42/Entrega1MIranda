from django.urls import path

from . import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('nuevoalumno' , views.nuevoalumno),
    path('nuevoprofe' , views.nuevoprofe),
    path('nuevocurso', views.nuevocurso),
]