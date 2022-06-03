from django import forms


class CursoFormulario(forms.Form):

    
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfeFormulario(forms.Form):

    
    nombre = forms.CharField()
    apellido = forms.CharField()



class AlumnoFormulario(forms.Form):

    
    nombre = forms.CharField()
    apellido = forms.CharField()