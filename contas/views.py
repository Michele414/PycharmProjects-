from django.shortcuts import render,redirect
from .models import transaçao
import datetime
from .form import transaçaoform 


 #Create your views here.

def  home (request):
     data = {}
     data['transaçoes'] = ['t1', 't2', 't3']
     return render (request,'contas/home.html',data)

def listagem(request):
    data = {}
    #data ["transaçoes"] = transaçao.objects.all()
    return render (request,'contas/listagem.html',data)

def nova (request):
     data = {}
     form = transaçaoform(request.POST or None)

     if form.is_valid():
          form.save()
          return redirect ('url_listagem')

     data ['form'] = form
     return render (request, 'contas/transaçaoform.html',data)
      
def update(request,pk):
     data = {}
     transaçao = transaçao.objects.filter(pk=pk) 
     form = transaçaoform(request.POST or None,instance=transaçao) 

     if form.is_valid():
          form.save()
          return redirect ('url_listagem')

     data ['form'] = form
     data['transaça'] = transaçao
     return render (request, 'contas/form.html',data)

def delete (request,pk):
     transaçao = transaçao.objects,get(pk=pk)
     transaçao.delete()
     return redirect ('url_listagem')
