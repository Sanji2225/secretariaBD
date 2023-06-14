from django.db import models


sexo =     [('M', 'Masculino'), 
            ('F', 'Feminino')]

class aluno(models.Model):
    matricula=models.IntegerField(primary_key=True)
    nomea=models.CharField(max_length=30)
    sexoa= models.CharField(max_length=1, choices=sexo)
    curso=models.CharField(max_length=30)
    cpf=models.CharField(max_length=11)
    endereco=models.CharField(max_length=60)
    celular=models.CharField(max_length=11)


    def __str__(self) -> str:
        return self.nomea
    class Meta:
        managed=False
        db_table='aluno'
        verbose_name='Aluno'
class professor(models.Model):
    masp= models.IntegerField(primary_key=True, null=False)
    nomep= models.CharField(max_length=30, null=False)
    dep = models.CharField(max_length=3)
    sexop= models.CharField(max_length=1, choices=sexo)
    
    def __str__(self) -> str:
        return self.nomep
    class Meta:
        managed=False
        db_table='professor'
        verbose_name='Professore'


class disciplina(models.Model):
    class per(models.IntegerChoices):
        Primeiro = 1
        Segundo = 2        
    
    cod_disc=models.IntegerField(primary_key=True, null=False)
    masp=models.ForeignKey(professor, null=False, on_delete=models.CASCADE)
    cargahp=models.IntegerField()
    cargaht=models.IntegerField()
    periodo=models.IntegerField(choices=per.choices)
    nomed=models.CharField(max_length=40, null=False)

    def __str__(self) -> str:
        return self.nomed
    class Meta:
        managed=False
        db_table='disciplina'
        verbose_name='Disciplina'

class orienta(models.Model):
    cod_o = models.ForeignKey(professor, null=False, on_delete=models.CASCADE)
    matricula_o=models.ForeignKey(aluno, null=False, on_delete=models.CASCADE, primary_key=True)


    def __int__(self) -> str:
        return self.matricula_o
    class Meta:
        managed=False
        db_table='orienta'
        verbose_name='Orientações'
    
class cursar(models.Model):
    cod_c=models.ForeignKey(disciplina, on_delete=models.CASCADE, primary_key=True, null=False)
    cod_a=models.ForeignKey(aluno, on_delete=models.CASCADE)

    def __int__(self) -> str:
        return self.cod_a
    class Meta:
        managed=False
        db_table='cursar'
        verbose_name='Matriculas em Disciplina'