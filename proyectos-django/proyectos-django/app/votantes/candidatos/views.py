
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django import forms
from .forms import FormCandidato, FormCandidatoEditar, FormPartido, FormFiltrosCandidato
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Candidato, Partido, Votacion
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Count
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def lista_candidatos(request):
    temp = Candidato.objects.all()
    if request.method == 'POST':
        form = FormFiltrosCandidato(request.POST)
        nombre = request.POST.get('nombre', None)
        ap = request.POST.get('apeido_paterno', None)
        am = request.POST.get('apeido_materno', None)
        partido = request.POST.get('partidos', None)
        cantidad_seleccionada = int(request.POST.get('cuantos', 10))
        if nombre:
            temp = temp.filter(nombre__icontains=nombre)
        if ap:
            temp = temp.filter(ap__icontains=ap)
        if am:
            temp = temp.filter(am__icontains=am)
        if partido:
            temp = temp.filter(partidos__nombre__icontains=partido)
    else:
        form = FormFiltrosCandidato()
        cantidad_seleccionada = 5
    
    paginator = Paginator(temp, cantidad_seleccionada)  # Show 5 candidatos per page.
    page_number = request.GET.get('page')
    candidatos = paginator.get_page(page_number)
    context = {'candidatos': candidatos, 'form': form, 'cuantos': cantidad_seleccionada}
    return render(request, 'lista_candidatos.html', context)

def eliminar_candidato(request, id):

    programa = Candidato.objects.filter(id=id)
    programa.delete()
        
    return redirect('lista_candidatos')
def votar_candidato(request, id):
    try:
        candidato = Candidato.objects.get(id=id)
        votacion = Votacion(candidato=candidato)
        votacion.save()
        return redirect('votaciones')
    except Candidato.DoesNotExist:
        return HttpResponse("El candidato no existe", status=404)
def eliminar_partido(request, id):
    Partido.objects.get(id=id).delete()
    return redirect('lista_Partidos')

class CrearCandidatosView(CreateView):
    model = Candidato
    form_class = FormCandidato
    success_url = reverse_lazy('lista_candidatos')
    success_message = "Datos guardados de manera exitosa"

class EditarCandidatoView(UpdateView):
    model = Candidato
    form_class = FormCandidato
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_candidatos')

class CrearPartidoView(CreateView):
    model = Partido
    form_class = FormPartido
    success_url = reverse_lazy('lista_partidos')
    success_message = "Datos guardados de manera exitosa"

class EditarPartidoView(UpdateView):
    model = Partido
    form_class = FormPartido
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_partidos')

class ListaPartido(ListView):
    model = Partido
    
def votaciones(request):
    temp = Candidato.objects.all()
    if request.method == 'POST':
        form = FormFiltrosCandidato(request.POST)
        nombre = request.POST.get('nombre', None)
        ap = request.POST.get('apeido_paterno', None)
        am = request.POST.get('apeido_materno', None)
        partido = request.POST.get('partidos', None)
        cantidad_seleccionada = int(request.POST.get('cuantos', 10))
        if nombre:
            temp = temp.filter(nombre__icontains=nombre)
        if ap:
            temp = temp.filter(ap__icontains=ap)
        if am:
            temp = temp.filter(am__icontains=am)
        if partido:
            temp = temp.filter(partidos__nombre__icontains=partido)
    else:
        form = FormFiltrosCandidato()
        cantidad_seleccionada = 5
    
    paginator = Paginator(temp, cantidad_seleccionada)  # Show 5 candidatos per page.
    page_number = request.GET.get('page')
    candidatos = paginator.get_page(page_number)
    context = {'candidatos': candidatos, 'form': form, 'cuantos': cantidad_seleccionada}
    return render(request, 'votaciones.html', context)
def lista_candidatos_puntuacion(request):
    candidatos_con_votos = Candidato.objects.annotate(num_votos=Count('votacion'))
    context = {'candidatos': candidatos_con_votos}
    return render(request, 'lista_candidatos_puntuacion.html', context)

class Grafica(TemplateView):
    template_name="grafica.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        votos = Candidato.objects.annotate(num_votos=Count('votacion')).order_by('-num_votos')
        
        nombres_candidatos = [candidato.nombre for candidato in votos]
        num_votos = [candidato.num_votos for candidato in votos]

        # Pasar los datos al contexto
        context['nombres_candidatos'] = nombres_candidatos
        context['num_votos'] = num_votos

        return context
    
def homepage(request):
    template = loader.get_template('grafica.html')
    context = {}
    return HttpResponse(template.render(context, request))