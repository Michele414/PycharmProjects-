from django.shortcuts import render,redirect
from .models import Transacao
import datetime
from .form import TransacaoForm


 #Create your views here.

def  home (request):
     data = {}
     data['Transacoes'] = ['t1', 't2', 't3']
     return render (request ,'contas/home.html',data)

def listagem(request):
    data = {}
    data ['transacoes'] = Transacao.objects.all()
    return render (request,'contas/listagem.html',data)

def nova (request):
     data = {}
     form = TransacaoForm (request.POST or None)

     if form.is_valid():
          form.save()
          return redirect ('url_listagem')

     data ['form'] = form
     return render (request, 'contas/transaçaoform.html',data)
      
def update(request,pk):
     data = {}
     transacao = 'transacao.objects.filter (pk=pk)' 
     form = TransacaoForm(request.POST or None,instance=transacao) 

     if form.is_valid():
          form.save()
          return redirect ('url_listagem')

     data ['form'] = form
     data['transacao'] = transacao
     return render (request, 'contas/form.html',data)

def delete (request,pk):
    transacao = Transacao.objects.all(pk=pk)
    transacao.delete()
    return redirect ('url_listagem')
