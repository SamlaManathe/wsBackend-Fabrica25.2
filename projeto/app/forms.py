from django import forms
from .models import Estado

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla', 'regiao', 'descricao', 'imagem']

class EstadoEditForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['descricao', 'imagem']

