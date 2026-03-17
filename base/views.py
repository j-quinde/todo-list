from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from base.models import Tarea
from .forms import TareaForm


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

class RegistroUsuario(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    # redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    def dispatch(self, request, *args, **kwargs):
        # si el usuario ya esta logueado, redirigir
        if request.user.is_authenticated:
            return redirect('tareas')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(RegistroUsuario, self).form_valid(form)

# Vista tareas
class ListaTareas(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()
        context['form'] = TareaForm()

        valor_buscado = self.request.GET.get('buscador') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


# class CrearTarea(LoginRequiredMixin,CreateView):
#     model = Tarea
#     fields = ['titulo','descripcion','completo']
#     success_url = reverse_lazy('tareas')
#
#     def form_valid(self, form):
#         form.instance.usuario = self.request.user #automaticamente asigna el valor de la instancia al usuario logeado
#         return super(CrearTarea,self).form_valid(form)

@login_required
def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('tareas')
    return redirect('tareas')
    # else:
    #     form = TareaForm()
    # return render(request,'base/tarea_form.html',{'form':form})


class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

# class EliminarTarea(DeleteView):
#     model = Tarea
#     context_object_name = 'tareas'
#     success_url = reverse_lazy('tareas')

@login_required # para funciones se usan decoradores
def eliminarTarea(request,pk):
    tarea = get_object_or_404(Tarea,pk=pk)
    tarea.delete()
    messages.success(request,'Tarea eliminado correctamente')
    return redirect('tareas')

def actualizarTarea(request,pk):
    tarea = get_object_or_404(Tarea,pk=pk)
    if request.method == 'POST':
        tarea.completo = "completo" in request.POST
        tarea.save()
        return JsonResponse({"success":True,"completo": tarea.completo})
    return JsonResponse({"success":False}, status=400)