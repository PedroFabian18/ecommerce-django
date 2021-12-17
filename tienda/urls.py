from django.urls import path
from . import views

urlpatterns = [
    path('',views.tienda, name = 'tienda'),
    path('<slug:categoria_slug>/', views.tienda, name = 'productos_por_categoria'),
    path('<slug:categoria_slug>/<slug:product_slug>/', views.product_detail, name = 'product_detail'),
]
