from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Publicacoes(models.Model):
    descricao_publicacao= models.TextField()
    data_criacao= models.DateTimeField(auto_now=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'publicacoes'

    def __str__(self):
        return self.descricao_publicacao
    

class Usuarios(models.Model):
    nome= models.CharField(max_length=100)
    email= models.CharField(max_length=100, unique=True)
    senha= models.TextField()
    data_criacao=models.DateTimeField(auto_now=True)
    is_instagram_admin= models.IntegerField()

    class Meta:
        db_table = 'usuarios'
