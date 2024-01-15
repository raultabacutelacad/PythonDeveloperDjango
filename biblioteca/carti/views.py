from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CarteForm

def adauga_carte(request):
    if request.method == 'POST':
        form = CarteForm(request.POST)
        if form.is_valid():
            form.save()
            print(f"Carte adaugata: {form.cleaned_data['titlu']}, {form.cleaned_data['autor']}, {form.cleaned_data['descriere']}")
            return redirect('adauga_carte')
    else:
        form = CarteForm()

    return render(request, 'carti/adauga_carte.html', {'form': form})