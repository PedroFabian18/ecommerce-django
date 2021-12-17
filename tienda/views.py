from django.shortcuts import render, get_object_or_404
from .models import Producto
from categorias.models import Categoria

# Create your views here.
def tienda(request, categoria_slug = None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug = categoria_slug)
        productos = Producto.objects.filter(categoria = categorias, is_available = True)
        cantidad_productos = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available = True)
        cantidad_productos = productos.count()

    context = {
        'productos' : productos,
        'cantidad_productos' : cantidad_productos,
        }

    return render(request,'tienda/tienda.html', context)

def product_detail(request, categoria_slug, product_slug):
    try:
        single_product = Producto.objects.get(categoria__slug = categoria_slug, slug = product_slug)
    except Exception as e:
        raise # -*- coding: utf-8 -*-

    context = {
    'single_product': single_product,
    }

    return render(request, 'tienda/product_detail.html', context)
