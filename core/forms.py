from django import forms
from .models import *

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nome', 'descricao']

class PalavraForm(forms.ModelForm):
    class Meta:
        model = Palavra
        fields = ['tema', 'palavra', 'dica']
        widgets = {
            'tema': forms.Select(attrs={'class': 'form-control'}),
            'palavra': forms.TextInput(attrs={'class': 'form-control'}),
            'dica': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)

        if professor:
            self.fields['tema'].queryset = Tema.objects.filter(professor=professor)

        self.fields['dica'].required = False