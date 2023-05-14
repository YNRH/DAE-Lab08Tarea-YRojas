from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Producto
from .models import Categoria

def index(request):
    #produc_list = Producto.objects.order_by('nombre')[:6]
    product_list = Producto.objects.all()
    category_list = Categoria.objects.all()
    context = {
        'productos': product_list,
        'categorias': category_list
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    category_list = Categoria.objects.all()
    context = {
        'productos': producto,
        'categorias': category_list,
    }
    return render(request,'producto.html', context)

def categoria(request, categoria_id):
    category = get_object_or_404(Categoria, pk=categoria_id)
    product_list = Producto.objects.filter(categoria=category)
    category_list = Categoria.objects.all()
    context = {
        'productos': product_list,
        'categorias': category_list,
    }
    return render(request, 'index.html', context)