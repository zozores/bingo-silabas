from django.contrib import admin
from .models import Silaba, Compartilhamento

@admin.register(Silaba)
class SilabaAdmin(admin.ModelAdmin):
    list_display = ('silaba', 'palavra1', 'palavra2', 'imagem1', 'imagem2')
    search_fields = ('silaba', 'palavra1', 'palavra2')
    ordering = ('silaba', )

@admin.register(Compartilhamento)
class CompartAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', 'facebook', 'twitter', 'whatsapp', 'telegram', 'email')
    ordering = ('mes', 'ano')
