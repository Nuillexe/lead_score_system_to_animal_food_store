from django.contrib import admin
from .models import Lead

# Customiza a exibição do modelo no painel do admin
class LeadAdmin(admin.ModelAdmin):
    # Define quais campos vão aparecer como colunas na tabela de listagem
    list_display = ('nome', 'idade', 'renda','numero_pets', 'data_criacao','prefere_saco_racao', 'pontuacao')
    
    # Adiciona uma barra de pesquisa para buscar clientes pelo nome
    search_fields = ('nome',)
    search_fields = ('pontuacao',)
    search_fields = ('prefere_saco_racao',)
    
    # Adiciona filtros laterais automáticos
    list_filter = ('idade',)
    list_filter = ('prefere_saco_racao',)

# Registra o modelo usando as configurações customizadas que criamos acima
admin.site.register(Lead, LeadAdmin)