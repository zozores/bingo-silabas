from django.contrib import admin
from .models import Silaba, Metrica, Comentario

@admin.register(Silaba)
class SilabaAdmin(admin.ModelAdmin):
    list_display = ('silaba', 'palavra1', 'palavra2', 'imagem1', 'imagem2')
    search_fields = ('silaba', 'palavra1', 'palavra2')
    ordering = ('silaba', )

@admin.register(Metrica)
class MetricaAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', 'sorteios', 'facebook', 'twitter', 'whatsapp', 'telegram', 'email')
    ordering = ('mes', 'ano')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('publicado', 'nome', 'email', 'tipo', 'mensagem')
    list_filter = ('publicado', 'tipo', 'nome')
    search_fields = ('publicado', 'nome', 'tipo', 'mensagem')
    ordering = ('-publicado', 'nome' )
    date_hierarchy = 'publicado'
