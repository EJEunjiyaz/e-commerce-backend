from django.urls import path, include
from rest_framework_mongoengine import routers

from website import views

router = routers.DefaultRouter()
router.register(r'shopee_items', views.ShopeeItemViewSet)
router.register(r'product_categories', views.ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shopee_item/', views.post_shopee_item, name='post_shopee_item'),
    path('shopee_item_variations/', views.post_shopee_item_variations, name='post_shopee_item_variations')
]
