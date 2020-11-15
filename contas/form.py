from django.forms import ModelForm
from .models import transaçao



class transaçaoForm (ModelForm):
  class meta:
    model = transaçao
    fields = ['data','desscriçao','valor','observaçoes','categoria']
