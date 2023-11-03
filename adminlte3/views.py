from django.shortcuts import render, redirect, get_object_or_404
from .models import Municipio, Cisternas, Alimentos
from .forms import MunicipioForm, CisternasForm
from django.views.generic import ListView, DetailView, View
from .graph import get_graph

class IndexView(ListView):
    template_name = 'adminlte/municipio.html'
    context_object_name = 'municipio_list'
    
    
    def get_queryset(self):
        
        return Municipio.objects.all()

class IndexView3(ListView):
    template_name = 'adminlte/municipio.html'
    context_object_name = 'count'

    def get_queryset(self):  
        
        return Municipio.objects.count()

class EntregaSISAView(ListView):
    template_name = 'adminlte/sisa.html'
    context_object_name = 'entregaSISA'

    def get_queryset(self):
        tot_ali = Alimentos.objects.count()
        tot_ref = Municipio.objects.count() * 1000
        tot_lei = Municipio.objects.count() * 2500
        tot_cis = Cisternas.objects.count()


        graph = get_graph()

        entregaSISA = [tot_ali, tot_ref, tot_lei, tot_cis, graph ]
        
        return entregaSISA


def graph_view(request):
    # Get the graph
    graph = get_graph()

    # Render the graph to the template
    return render(request, 'adminlte/sisa.html', {'graph': graph})

class MinhaClasse:
    def __init__(self, atributo):
        self.atributo = atributo

class PesquiseAqui(ListView):     
    template_name = 'adminlte/sisa.html'
    context_object_name = 'PesquiseAqui'

    def get_queryset(self):
        queryset_a = Municipio.objects.all()
        queryset_b = Alimentos.objects.all()
        
        
        combined_queryset = queryset_a | queryset_b
        
        return combined_queryset

class AlimentosPeriodoListView(ListView):
    model = Alimentos
    template_name = 'adminlte/sisa_alimentos.html'
    context_object_name = 'AlimentosPeriodoListView'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        ctx = super(AlimentosPeriodoListView, self).get_context_data(**kwargs)
        # adiciona variável para exibir por padrão o filtro da pesquisa avançadan
        ctx['avancado'] = 'True'
        return ctx
    
    def get_queryset(self, **kwargs):
        
        qs = Alimentos.objects.raw('''
SELECT dat_ano, dat_mes, municipio.nom_municipio,  sum(qtd_alimento), sum(val_alimento), 1 as id
  FROM dados.alimentos, dados.municipio
where 
municipio.ide_municipio = alimentos.ide_municipio
group by  dat_ano, dat_mes,  municipio.nom_municipio, municipio.id
order by dat_ano, dat_mes desc, municipio.nom_municipio
''',
        )

        return qs
            



    


