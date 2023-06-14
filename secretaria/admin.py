from django.contrib import admin
from secretaria.models import aluno
from secretaria.models import professor
from secretaria.models import disciplina
from secretaria.models import orienta
from secretaria.models import cursar
# Register your models here.

admin.site.register(aluno)

admin.site.register(professor)

admin.site.register(disciplina)

admin.site.register(orienta)

admin.site.register(cursar)
