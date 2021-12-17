from .models import Categoria

# Se debe registrar en settings de ecommerce{TEMPLATES} para hacer publica esta funcion, para
# que cualquier template del proyecto pueda tener acceso a la lista de links

def menu_links(request):
    links = Categoria.objects.all()
    return dict( links = links)
