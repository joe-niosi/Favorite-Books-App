from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.home), #get, renders index.html    
    path('books/create', views. new_book), #POST, creates new book
    
]