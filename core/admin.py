from django.contrib import admin
from .models import Silaba

@admin.register(Silaba)
class SilabaAdmin(admin.ModelAdmin):
    list_display = ('silaba', 'palavra1', 'palavra2', 'imagem1', 'imagem2')
    search_fields = ('silaba', 'palavra1', 'palavra2')
    ordering = ('silaba', )
