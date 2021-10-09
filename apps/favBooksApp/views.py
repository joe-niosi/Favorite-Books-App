from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from apps.loginRegApp.models import *
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        'all_books': Book.objects.all(),
    }
    return render(request, 'home.html', context)

def new_book(request):
    if 'user_id' not in request.session:
        messages.error(request, "Access denied, must be logged in!")
        return redirect('/books')
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        creator = user
    )
    user.liked_books.add(book) # this make creator of the book automatically favorite the book
    print(book)
    return redirect('/books')
    
def one_book(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    all_books = Book.objects.get(id = book_id)
    context = {
        'user': user,
        'all_books': all_books,
    }
    return render(request, "one_book.html", context)