from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-person/', views.add_person, name='add_person')
]