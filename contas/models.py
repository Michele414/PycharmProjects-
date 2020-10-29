from django.db import models


# Create your models here.

class categoria(models.Model):
    nome=models.CharField(max_length=100)
    dt_criaçao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome


class transaçao (models.Model):
    data=models.DateTimeField(auto_now_add=True)
    descriçao=models.CharField(max_length=200)
    valor=models.DecimalField(max_digits=7,decimal_places=2)
    categoria= models.ForeignKey(categoria,on_delete=models.CASCADE)
    observaçoes=models.TextField()

class meta:
    verbose_name_plural='transaçoes'
   

       
