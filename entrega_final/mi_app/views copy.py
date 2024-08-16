from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
from django.urls import reverse_lazy

# Dejamos la vista INICIO basada en funciones y visible para todos
def inicio(request):
    return render(request, "mi_app/index.html")


# Dejamos una vista basada en funciones que requiere login para mostrar el uso de @login_required
@login_required
def about(request):
    return render(request, "mi_app/about.html")


# VISTAS BASADAS EN CLASES - AUTORES
class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "mi_app/autor_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
@login_required
def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'mi_app/autor_list.html', {'autores':  autores})

class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "mi_app/autor_detail.html"

    # AGREGADO!
    # Esta es otra forma para redirigir a un login. Tiene prioridad sobre la configuración del settings.py
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url
    
@login_required
def autor_detail(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return HttpResponseNotFound("Autor no encontrado")
    return render(request, 'mi_app/autor_detail.html', {'autor': autor})


class AutorCreateView(LoginRequiredMixin, CreateView):

    model = Autor
    template_name = "mi_app/autor_create.html"
    fields = ["nombre", "bio"]
    success_url = reverse_lazy("AutorList")

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

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = reverse_lazy("AutorList")
    fields = ["nombre", "bio"]
    template_name = "mi_app/autor_update.html"


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

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy("AutorList")
    template_name = 'mi_app/autor_confirm_delete.html'

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




# VISTAS BASADAS EN CLASES - LIBROS
class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "mi_app/libro_list.html"


class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "mi_app/libro_detail.html"


class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "mi_app/libro_create.html"
    fields = ["titulo", "editorial", "descripcion", "fecha"]
    success_url = reverse_lazy("LibroList")


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    success_url = reverse_lazy("LibroList")
    fields = ["titulo", "editorial", "descripcion", "fecha"]
    template_name = "mi_app/libro_update.html"


class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy("LibroList")
    template_name = 'mi_app/libro_confirm_delete.html'