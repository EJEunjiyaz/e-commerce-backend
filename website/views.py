from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')


def homepage_view(request):
    return render(request, 'homepage.html')


def add_product_view(request):
    return render(request, 'add_product.html')
