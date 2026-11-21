from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('playas/', views.lista_playas, name='lista_playas'),
    #path('playas/<str:nombre>/', views.detalle_playa, name='detalle_playa'),
]