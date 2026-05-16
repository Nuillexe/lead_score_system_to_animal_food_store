from django.contrib import admin
from .models import Lead

# Customiza a exibição do modelo no painel do admin
class LeadAdmin(admin.ModelAdmin):
    # Define quais campos vão aparecer como colunas na tabela de listagem
    list_display = ('nome', 'idade', 'renda', 'pontuacao')
    
    # Adiciona uma barra de pesquisa para buscar clientes pelo nome
    search_fields = ('nome',)
    
    # Adiciona filtros laterais automáticos
    list_filter = ('idade',)

# Registra o modelo usando as configurações customizadas que criamos acima
admin.site.register(Lead, LeadAdmin)