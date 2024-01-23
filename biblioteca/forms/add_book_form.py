from django import forms

rating = [
  (0, ""),
  (1, "⭐"),
  (2, "⭐⭐"),
  (3, "⭐⭐⭐"),
  (4, "⭐⭐⭐⭐"),
  (5, "⭐⭐⭐⭐⭐")
]

class AddBookForm(forms.Form):
  titlu = forms.CharField(label="Titlu Carte", max_length=256)
  autor = forms.CharField(label="Autor", max_length=100)
  descriere = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
  rating = forms.ChoiceField(choices = rating)
  imagine = forms.FileField()
