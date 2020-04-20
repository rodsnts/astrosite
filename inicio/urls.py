from django.urls import path
from .views import home

urlpatterns = [
    path('',home),
]

#ciclo de vida de uma aplicação 
#request > url> view >model> response