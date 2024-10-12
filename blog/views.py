from django.shortcuts import render

def lista_blog(request):
    return render(request,'lista_blog.html')

def detalle(request):
    return render(request,'detalle_blog.html')



# Create your views here.
