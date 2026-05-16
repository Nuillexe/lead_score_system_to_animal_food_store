from django.shortcuts import render
from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields= ['nome', 'idade', 'renda']


def avaliar_lead(request):
    pontuacao_final=None
    
    if request.method =='POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead=form.save(commit=False)
            pontos=0

            if lead.idade>=25 and lead.idade<=45:
                pontos+=30
            else:
                pontos+=10
           
            #Regra por Renda
            if lead.renda>= 5000:
                pontos += 50
                
            elif lead.renda>=2000:
                pontos+=20
            else:
                pontos+=5

                #Salva a pontuação calculada no objto
            lead.pontuacao=pontos
            lead.save()

            pontuacao_final=pontos
    else:
        form=LeadForm()

    return render(request, 'lead_form.html', {'form': form, 'pontuacao': pontuacao_final})
                


