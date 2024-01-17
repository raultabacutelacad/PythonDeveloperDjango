
from django.shortcuts import render, get_object_or_404, redirect

from biblioteca.models import Carte

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

def rate(request, id):
    if request.method == "POST":
        print(request.POST)
    return render(request, "rating.html")



