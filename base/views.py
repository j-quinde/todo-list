from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from base.models import Tarea

# LoginRequiredMixin: protege las vistas basadas en clases (CBV)
# restringiendo el acceso solo a usuarios autenticados

# Create your views here.
class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    # reescribir un metodo, una vez logueado
    # te manda a la pagina principal de tareas
    def get_success_url(self):
        return reverse_lazy('tareas')


#class Logout(LogoutView):

# Vista tareas
class ListaTareas(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = 'tareas'


class CrearTarea(CreateView):
    model = Tarea
    fields = ['titulo','descripcion','completo']
    success_url = reverse_lazy('tareas')

class EditarTarea(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

# class EliminarTarea(DeleteView):
#     model = Tarea
#     context_object_name = 'tareas'
#     success_url = reverse_lazy('tareas')

def eliminarTarea(request,pk):
    tarea = get_object_or_404(Tarea,pk=pk)
    tarea.delete()
    messages.success(request,'Tarea eliminado correctamente')
    return redirect('tareas')