from django.shortcuts import render
from .models import transaçao
import datetime 


 #Create your views here.

def  home (request):
     data = {}

     return render (request,'contas/home.html',data)

def listagem(request):
  data = {}
  data["transaçoes"]= transaçao.objects.all()
  return render (request,'contas/listagem.html',data)
      