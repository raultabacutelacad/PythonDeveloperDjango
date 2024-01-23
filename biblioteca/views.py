
from django.shortcuts import render, get_object_or_404, redirect
from biblioteca.forms.add_book_form import AddBookForm
from biblioteca.forms.rate_book_form import RateBookForm

from biblioteca.models import Carte

def confirm_marcheaza_ca_citit(request,id_carte):
    carte = get_object_or_404(Carte, pk=id_carte)
    return render(request, 'marcheaza_ca_citit.html', {'carte': carte})

def marcheaza_ca_citit(request, id_carte):
    carte = get_object_or_404(Carte, pk=id_carte)
    carte.citit =1 
    carte.save()
    return redirect('homepage')

def rating_carte(request, id_carte):
    carte = get_object_or_404(Carte, pk=id_carte)
    if request.method == "POST":
        form = RateBookForm(request.POST)
        if form.is_valid():
            carte.rating = form.data['rating']
            carte.save()
        return redirect('homepage') 
    else:   
        form = RateBookForm()
        return render(request, 'rate_book.html', {'form': form, 'carte': carte})

def adauga_carte(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            carte_noua = Carte(
                titlu = form.data['titlu'],
                autor = form.data['autor'],
                descriere = form.data['descriere'],
                citit = 0,
                rating = form.data['rating'],
                imagine = form.files['imagine']
            )
            carte_noua.save()
        return redirect('homepage')
    else: 
        form = AddBookForm()
        return render(request, 'add_book.html', {'form': form})

def homepage(request):        
    carti = Carte.objects.all()
    return render(request, 'homepage.html', {'carti': carti})               

def delete_book(request, book_id):
    book = get_object_or_404(Carte, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('homepage')
    return redirect('delete_book', book_id=book_id)


def confirm_delete_book(request, book_id):
    book = get_object_or_404(Carte, pk=book_id)
    return render(request, 'delete_book.html', {'book': book})



