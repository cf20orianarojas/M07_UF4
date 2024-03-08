from django.urls import path
from . import views

urlpatterns = [
    # truca 'index' de la view
    path('', views.index, name='index')
]