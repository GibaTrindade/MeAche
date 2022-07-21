from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Lugar, Comodo, Compartimento, Objeto, HistoricoTransferencias
from .forms import LugarForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	lugares = Lugar.objects.filter(autor = request.user)
	#import pdb;pdb.set_trace()

	return render(request, 'home.html', {'lugares': lugares})

def lista_lugares(request):
	lugares = Lugar.objects.all()
	#import pdb;pdb.set_trace()

	return render(request, 'lista_lugares.html', {'lugares': lugares})

@login_required
def lista_objetos(request):
	objetos = Objeto.objects.filter(autor = request.user).order_by('compartimento__comodo__lugar__nome', 'compartimento__comodo__nome', 'compartimento__nome')

	return render(request, 'lista_objetos.html', {'objetos':objetos})

@login_required
def detalhe_lugar(request, pk):
	lugar = Lugar.objects.get(pk=pk, autor = request.user)
	comodos = Comodo.objects.filter(lugar_id=pk, autor = request.user)
	return render(request, 'detalhe_lugar.html', {'lugar': lugar, 'comodos': comodos})

@login_required
def detalhe_comodo(request, pk):
	comodo = Comodo.objects.get(pk=pk, autor = request.user)
	compartimentos = Compartimento.objects.filter(comodo_id=pk, autor = request.user)
	return render(request, 'detalhe_comodo.html', {'comodo': comodo, 'compartimentos': compartimentos})

@login_required
def detalhe_compartimento(request, pk):
	compartimento = Compartimento.objects.get(pk=pk, autor = request.user)
	objetos = Objeto.objects.filter(compartimento_id=pk, autor = request.user)
	return render(request, 'detalhe_compartimento.html', {'compartimento': compartimento, 'objetos': objetos})

@login_required
def detalhe_objeto(request, pk):
	#objeto = Objeto.objects.get(pk=pk, autor = request.user)
	objeto = get_object_or_404(Objeto, pk=pk, autor = request.user)
	return render(request, 'detalhe_objeto.html', {'objeto': objeto})

@login_required
def transfere_objeto(request, pk):
	objeto = Objeto.objects.get(pk=pk,autor = request.user)
	compartimentos = Compartimento.objects.filter(autor = request.user).order_by('comodo__lugar__nome', 'comodo__nome')
	return render(request, 'transfere_objeto.html', {'objeto': objeto, 'compartimentos':compartimentos})

@login_required
def efetuar_transferencia(request, pk, obj):
	objeto = Objeto.objects.get(pk=obj, autor = request.user)
	compartimentoPara = Compartimento.objects.get(pk=pk, autor = request.user)
	compartimentoDe = Compartimento.objects.get(pk=objeto.compartimento_id)
	historico = HistoricoTransferencias.objects.create(objeto=objeto, compartimentoDe=compartimentoDe, compartimentoPara=compartimentoPara)
	objeto.compartimento_id = compartimentoPara.id
	
	objeto.save()
	historico.save()
	
	messages.success(request, 'Objeto Tranferido com sucesso!')
	return redirect('lista_objetos')
#class ListaLugares(ListView):
#	model = Lugar
#	template_name = 'home.html'