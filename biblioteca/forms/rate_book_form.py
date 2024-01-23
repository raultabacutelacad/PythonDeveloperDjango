from django import forms 


rating = [
  (0, ""),
  (1, "⭐"),
  (2, "⭐⭐"),
  (3, "⭐⭐⭐"),
  (4, "⭐⭐⭐⭐"),
  (5, "⭐⭐⭐⭐⭐")
]

class RateBookForm(forms.Form):
  rating = forms.ChoiceField(choices=rating)
  