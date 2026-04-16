from django import forms
from .models import Pessoa
from .models import Contato


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'idade']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'menssagem']

