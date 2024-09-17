
from django.contrib import admin
from .models import *

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'professor')
    search_fields = ('nome', 'descricao')
    list_filter = ('professor',)

class PalavraAdmin(admin.ModelAdmin):
    list_display = ('palavra', 'tema', 'dica')
    search_fields = ('palavra', 'tema__nome', 'dica')
    list_filter = ('tema',)

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'tema', 'data', 'resultado')
    search_fields = ('aluno__username', 'tema__nome', 'resultado')
    list_filter = ('tema', 'resultado', 'data')

# Registra os modelos com suas configurações
admin.site.register(Tema, TemaAdmin)
admin.site.register(Palavra, PalavraAdmin)
admin.site.register(Atividade, AtividadeAdmin)