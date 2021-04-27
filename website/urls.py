from django.urls import path

from .views import login_view, homepage_view, add_product_view

urlpatterns = [
    path('', login_view),
    path('homepage.html', homepage_view),
    path('add_product.html', add_product_view),
]
