from django.urls import path
from mi_app import views
from .views import buscar_libros

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about/', views.about, name="About")
]

# Libros
urlpatterns += [
    path('buscar-libros/', buscar_libros, name='buscar_libros'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libro/<int:pk>/', views.libro_detail, name='libro_detail'),
    path('libro/crear/', views.libro_create, name='libro_create'),
    path('libro/<int:pk>/editar/', views.libro_update, name='libro_update'),
    path('libro/<int:pk>/eliminar/', views.libro_delete, name='libro_delete'),
]

# Autores
urlpatterns += [
    path('autores/', views.autor_list, name='autor_list'),
    path('autor/<int:pk>/', views.autor_detail, name='autor_detail'),
    path('autor/crear/', views.autor_create, name='autor_create'),
    path('autor/<int:pk>/editar/', views.autor_update, name='autor_update'),
    path('autor/<int:pk>/eliminar/', views.autor_delete, name='autor_delete'),
]