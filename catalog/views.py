from django.shortcuts import render

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)
