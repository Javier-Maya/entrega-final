from django import forms
from mi_app.models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'bio']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'editorial', 'genero', 'descripcion', 'fecha']
        widgets ={
            'genero': forms.Select(choices=[
                ('novela', 'Novela'),
                ('fantasia', 'Fantasia'),
                ('aventuras', 'Aventuras')

            ])
        }