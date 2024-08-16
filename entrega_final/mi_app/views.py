from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# Dejamos la vista INICIO basada en funciones y visible para todos
def inicio(request):
    return render(request, "mi_app/index.html")


# Dejamos una vista basada en funciones que requiere login para mostrar el uso de @login_required
@login_required
def about(request):
    return render(request, "mi_app/about.html")


# Vistas para Libro    
@login_required
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'mi_app/libro_list.html', {'libros':  libros})
    
@login_required
def libro_detail(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponseNotFound("Libro no encontrado")
    return render(request, 'mi_app/libro_detail.html', {'libro': libro})

@login_required
def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 'mi_app/libro_form.html', {'form': form, 'title': 'Crear Libro'})

@login_required
def libro_update(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponseNotFound("Libro no encontrado")
    
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'mi_app/libro_form.html', {'form': form, 'title': 'Actualizar Libro'})

@login_required
def libro_delete(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponseNotFound("Libro no encontrado")
    
    if request.method == "POST":
        libro.delete()
        return redirect('libro_list')
    return render(request, 'mi_app/libro_confirm_delete.html', {'libro': libro})


# Vistas para Autor    
@login_required
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'mi_app/autor_list.html', {'autores':  autores})
    
@login_required
def autor_detail(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponseNotFound("Autor no encontrado")
    return render(request, 'mi_app/autor_detail.html', {'autor': autor})

@login_required
def autor_create(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'mi_app/autor_form.html', {'form': form, 'title': 'Crear Autor'})

@login_required
def autor_update(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponseNotFound("Autor no encontrado")
    
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'mi_app/autor_form.html', {'form': form, 'title': 'Actualizar Autor'})

@login_required
def autor_delete(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponseNotFound("Autor no encontrado")
    
    if request.method == "POST":
        autor.delete()
        return redirect('autor_list')
    return render(request, 'mi_app/autor_confirm_delete.html', {'autor': autor})

def buscar_libros(request):
    query = request.GET.get('q', '')

    if query:
        # Filtrar los libros que coincidan con la búsqueda
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        # Si no hay búsqueda, mostrar todos los libros
        libros = Libro.objects.all()
    
    return render(request, "mi_app/buscar_libros.html", {
        'libros': libros,
        'query': query
    })