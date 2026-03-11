from django.urls import path
from .views import ListaTareas, CrearTarea, EditarTarea, eliminarTarea, Login, RegistroUsuario, actualizarTarea
from django.contrib.auth.views import LogoutView
urlpatterns = [path('',ListaTareas.as_view(), name='tareas'),
               path('login/', Login.as_view(), name='login'),
               path('registro/', RegistroUsuario.as_view(), name='registro'),
               path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
               path('crear-tarea/',CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>',EditarTarea.as_view(),name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', eliminarTarea,name='eliminar-tarea'),
               path('actualizar-tarea/<int:pk>', actualizarTarea, name='actualizar-tarea'),]