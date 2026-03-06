from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from base.models import Tarea


# Create your views here.

# Vista tareas
class ListaTareas(ListView):
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