from django import forms
from .models import Carte

class CarteForm(forms.ModelForm):
    class Meta:
        model = Carte
        #fields = ['titlu', 'autor', 'descriere']
        fields = ['titlu', 'autor', 'descriere', 'citit', 'rating', 'imagine']
    #
    # citit = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput())
    #
    # rating = forms.IntegerField(required=False)