from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.home), #get, renders index.html    
    path('books/create', views. new_book), #POST, creates new book
    path('books/<int:book_id>', views.one_book), #get, renders one_book.html
]