import requests
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView, 
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Estado, PontoTuristico
from .forms import EstadoForm, EstadoEditForm
from django.db.models import Q

# Create your views here.

class EstadoListView(ListView):
    model = Estado
    template_name = 'app/estado_list.html'
    context_object_name = 'estados'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(Q(nome__icontains=search) | Q(sigla__icontains=search))
        return queryset

class EstadoDetailView(DetailView):
    model = Estado
    template_name = 'app/estado_detail.html'
    context_object_name = 'estado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sigla = self.object.sigla

        url_cidades = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios'
        try:
            response_cidades = requests.get(url_cidades, timeout=5)
            response_cidades.raise_for_status()
            municipios = response_cidades.json()
        except requests.RequestException:
            municipios = []
        context['municipios'] = municipios

        context['regiao_nome'] = getattr(self.object, 'regiao', '')

        pontos = PontoTuristico.objects.filter(estado=self.object)
        context['pontos'] = pontos

        return context

class EstadoCreateView(CreateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'app/estado_form.html'
    success_url = reverse_lazy('estado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estado'] = None 
        return context

class EstadoUpdateView(UpdateView):
    model = Estado
    form_class = EstadoEditForm
    template_name = 'app/estado_form.html'
    success_url = reverse_lazy('estado_list')

class EstadoDeleteView(DeleteView):
    model = Estado
    template_name = 'app/estado_delete.html'
    success_url = reverse_lazy('estado_list')
        

