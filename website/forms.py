import re

from django import forms

from .models import Jogador


class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ["nome", "telefone", "campus"]

    def clean_telefone(self):
        return re.sub(r"\D", "", self.cleaned_data["telefone"])