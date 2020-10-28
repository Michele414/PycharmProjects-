from django.shortcuts import render
from django.http import HttpResponse
import datatime


# Create your views here.
def home (request):
    now=datatime.datatime.now()
    #html = "<html><body>It is now %s.</body></html>" % now

    return render(request,'contas/home.html')
