from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_lugares/', views.lista_lugares, name='lista_lugares'),
    path('lugar/<int:pk>/', views.detalhe_lugar, name="detalhe_lugar"),
    path('comodo/<int:pk>/', views.detalhe_comodo, name="detalhe_comodo"),
    path('compartimento/<int:pk>/', views.detalhe_compartimento, name="detalhe_compartimento"),
    path('objeto/<int:pk>/', views.detalhe_objeto, name="detalhe_objeto"),
    path('lista_objetos/', views.lista_objetos, name="lista_objetos"),
    path('transfere_objeto/<int:pk>/', views.transfere_objeto, name="transfere_objeto"),
    path('efetuar_transferencia/<int:pk>/<int:obj>/', views.efetuar_transferencia, name="efetuar_transferencia"),
]