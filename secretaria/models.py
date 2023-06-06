from django.db import models

class professor(models.Model):
    MASP=models.IntegerField(max_length=11)
    dep=models.CharField(max_length=3)
    nomep=models.CharField(max_length=30)
    sexop=[('M'), ('F')]
    titulo=models.CharField(max_length=2)

class aluno(models.Model):
    matricula=models.IntegerField(max_length=11)
    nomea=models.CharField(max_length=30)
    sexoa= [('M'), ('F')]
    curso=models.CharField(max_length=30)
    cpf=models.CharField(max_length=11)
    endereco=models.CharField(max_length=60)
    celular=models.CharField(max_length=11)

#class disciplina(models.Model):
 #   cod_disc=models.IntegerField(max_length=9)
  #  MASP=models.ForeignKey
