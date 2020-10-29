from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime 


# Create your views here.
def home (request):
  #data = {}
 # data['now'] = datetime.datetime.now()
 # html = "<html><body>It is now %s.</body></html>" % now
 return render (request,'contas/home.html',)

        