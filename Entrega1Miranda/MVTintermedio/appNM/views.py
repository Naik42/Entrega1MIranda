from django.shortcuts import render
from appNM.models import *
from appNM.forms import *
from appNM.templates import *

# Create your views here.
def inicio(request):
    return render(request, "appNM/inicio.html")





def cursos(request):

    return render(request, "appNM/cursos.html")





def estudiantes(request):

    return render(request, "appNM/estudiantes.html")





def profesores(request):

    return render(request, "appNM/profesores.html")




def nuevocurso(request):
    

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        

        if miFormulario.is_valid:

         info = miFormulario.cleaned_data
        
         curso = Curso (nombre=info['curso'], camada=info['camada'])
         
         curso.save()
         
         return render(request, "appNM/nuevocurso.html")

    else: 

            miFormulario= CursoFormulario()

            return render(request, "appNM/nuevocurso.html", {"miFormulario":miFormulario})



def nuevoprofe(request):

    if request.method == 'POST':

        miFormulario = ProfeFormulario(request.POST)


        if miFormulario.is_valid:

         info = miFormulario.cleaned_data
        
         profe = Profesor (nombre=info['nombre'], apellido=info['apellido'])
         
         profe.save()
         
         return render(request, "appNM/profesores.html")

    else: 

            miFormulario= ProfeFormulario()

            return render(request, "appNM/nuevoprofe.html", {"miFormulario":miFormulario})



def nuevoalumno(request):

    if request.method == 'POST':

        miFormulario = AlumnoFormulario(request.POST)

        

        if miFormulario.is_valid:

         info = miFormulario.cleaned_data
        
         profe = Estudiante (nombre=info['nombre'], apellido=info['apellido'])
         
         profe.save()
         
         return render(request, "appNM/inicio.html")

    else: 

            miFormulario= AlumnoFormulario()

            return render(request, "appNM/estudiantes.html", {"miFormulario":miFormulario})