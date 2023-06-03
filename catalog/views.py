from django.shortcuts import render

from catalog.models import Product


def product(request):
    product_list = Product.objects.all()
    content = {
        'object_list': product_list
    }


    return render(request, 'catalog/product.html', content)


def contacts(request):
    return render(request, 'catalog/contact.html')

def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/index.html', context)


def base(request):
    return render(request, 'catalog/base.html')
