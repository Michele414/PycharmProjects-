from django.contrib import admin
from .models import categoria
from .models import transaçao


# Register your models here.

admin.site.register(categoria)
admin.site.register(transaçao)