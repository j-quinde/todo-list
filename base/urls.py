from django.urls import path
from . import views
from .views import ListaTareas, CrearTarea, EditarTarea, eliminarTarea

urlpatterns = [path('',ListaTareas.as_view(), name='tareas'),
               path('crear-tarea/',CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>',EditarTarea.as_view(),name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', eliminarTarea,name='eliminar-tarea'),]