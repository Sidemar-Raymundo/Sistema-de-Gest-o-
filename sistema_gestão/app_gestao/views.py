from django.shortcuts import render , redirect
from .models import AvaliacaoFilme
from .forms import AvaliacaoFilmeForm





    

def itens(request):
    dados = {
        'dados':AvaliacaoFilme.objects.all()
    }
    return render(request, 'controle/itens.html',context=dados)

def detalhe(request, id_itens):
    dados = {'dados': AvaliacaoFilme.objects.get(pk=id_itens)}
    return render(request ,'controle/detalhe.html',dados)

def criar(request):
    if request.method == 'POST':
        item_forms = AvaliacaoFilmeForm(request.POST)
        if item_forms.is_valid():
            item_forms.save()
        return redirect('itens')
    
    itens_forms = AvaliacaoFilmeForm()
    formulario = {
            'formulario': itens_forms
        }
    return render(request,'controle/novo_item.html', context=formulario)
    
       
    
    
def editar(request, id_itens):  
    itens_f = AvaliacaoFilme.objects.get(pk=id_itens)
    # novo_investimento/ -> GET
    if request.method =='GET':
        formulario = AvaliacaoFilmeForm(instance= itens_f)
        return render(request,  'controle/novo_item.html', {'formulario': formulario})
    # caso requisição seja POST
    else:
        formulario = AvaliacaoFilmeForm(request.POST, instance= itens_f)
        if formulario.is_valid():
            formulario.save()
    return redirect('itens')


def excluir(request,id_itens):
    filme = AvaliacaoFilme.objects.get(pk=id_itens)
    if request.method == 'POST':
        filme.delete()  # Corrigi a linha aqui, alterando AvaliacaoFilme.delete() para item.delete()
        return redirect('itens')
    print(filme)
    return render(request, 'controle/confirmar_exclusao.html', {'item' :filme})

    
    