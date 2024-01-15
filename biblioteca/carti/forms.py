from django import forms
from .models import Carte

class CarteForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = ['titlu', 'autor', 'descriere']