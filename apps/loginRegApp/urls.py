from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #get, renders index.html
    path('register', views.register), #POST, creates new instance
    path('login', views.login), #GET, renders success.html
    path('logout', views.logout),
]