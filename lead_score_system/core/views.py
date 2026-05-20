from django.shortcuts import render
from django.contrib import messages
from .models import Lead

def avaliar_lead(request):
    pontuacao_final = None
    
    if request.method == 'POST':
        # 1. Captura os dados vindos direto do formulário HTML
        email = request.POST.get('email', '').strip()
        nome = request.POST.get('nome', '').strip()
        renda = request.POST.get('renda', '').strip()
        idade = request.POST.get('idade', '').strip()
        prefere_saco = request.POST.get('prefere_saco', '').strip()
        numero_pets = request.POST.get('numero_pets', '').strip()

        # 2. Validação: Verifica se algum campo foi enviado em branco
        if not all([email, nome, renda, idade, prefere_saco, numero_pets]):
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
            return render(request, 'lead_form.html')

        # 3. Validação: Verifica se o email já está cadastrado no banco de dados
        if Lead.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado em nosso sistema.")
            return render(request, 'lead_form.html')

        try:
            # 4. Cálculo da pontuação do Lead baseado nas regras do Pet Shop
            pontos = 0

            # Regra por Idade (Foco no público adulto tutor de pets)
            idade_int = int(idade)
            if 25 <= idade_int <= 45:
                pontos += 20
            else:
                pontos += 10
            
            # Regra por Renda (Maior poder de compra = maior pontuação)
            renda_decimal = float(renda)
            if renda_decimal >= 5000:
                pontos += 30
            elif renda_decimal >= 2000:
                pontos += 15
            else:
                pontos += 5

            # Regra por Preferência de Compra (Quem compra sacos fechados consome mais volume)
            venda_em_saco = (prefere_saco == 'sim')
            if venda_em_saco:
                pontos += 50
            else:
                pontos += 0

            # Regra por Número de Pets (Mais pets = maior gasto recorrente)
            pets_int = int(numero_pets)
            pontos+=30*pets_int

            # 5. Salva os dados tratados no modelo de banco de dados
            lead = Lead(
                email=email,
                nome=nome,
                renda=renda_decimal,
                idade=idade_int,
                prefere_saco_racao=venda_em_saco,
                numero_pets=pets_int,
                pontuacao=pontos
            )
            lead.save()

            # 6. Alerta de sucesso e passa o resultado para a tela
            messages.success(request, f"Cadastro realizado com sucesso! Obrigado, {nome}.")
            pontuacao_final = pontos

        except ValueError:
            messages.error(request, "Ocorreu um erro ao processar os valores numéricos. Tente novamente.")

    return render(request, 'lead_form.html', {'pontuacao': pontuacao_final})