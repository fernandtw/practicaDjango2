from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.lista_blog, name='lista_blog'),
    path('detalle/', views.detalle, name='detalle'),
]