from django.urls import path
from .import views

app_name = "tienda"
urlpatterns = [
    path('lista/', views.lista, name="lista"),
    path('detalle/', views.detalle, name="detalle" )
    
]