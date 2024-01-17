
from django.shortcuts import render, get_object_or_404, redirect

from biblioteca.forms import CarteForm
from biblioteca.models import Carte


# def adauga_carte(request):
#     if request.method == 'POST':
#         form = CarteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(f"Carte adaugata: {form.cleaned_data['titlu']}, {form.cleaned_data['autor']}, {form.cleaned_data['descriere']}")
#             return redirect('adauga_carte')
#     else:
#         form = CarteForm()
#
#     return render(request, 'adauga_carte.html', {'form': form})
#

def adauga_carte(request):
    if request.method == 'POST':
        form = CarteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(f"Carte adaugata: {form.cleaned_data['titlu']}, {form.cleaned_data['autor']}, {form.cleaned_data['descriere']}")
            return redirect('adauga_carte')
        else:
            print(form.errors)

    else:
        form = CarteForm()

    return render(request, 'adauga_carte.html', {'form': form})

def homepage(request):
     return "Hello"

def delete_book(request, book_id):
    book = get_object_or_404(Carte, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('homepage')
    return redirect('delete_book', book_id=book_id)


def confirm_delete_book(request, book_id):
    book = get_object_or_404(Carte, pk=book_id)
    return render(request, 'delete_book.html', {'book': book})



