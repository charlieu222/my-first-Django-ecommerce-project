from django.shortcuts import render
from .models import Product
# Create your views here.


def product_page(request):
    products = Product.objects.all()
    context = {
        "all_products": products

    }
    return render(request, "product.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def single_product_view(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }

    return render(request, "products_detail.html", context)
