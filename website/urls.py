from django.urls import path, include
from rest_framework_mongoengine import routers

from website import views
from website.views import ShopeeItemByCategory

router = routers.DefaultRouter()
router.register(r'shopee_items', views.ShopeeItemViewSet, basename='ShopeeItem')
router.register(r'product_categories', views.ProductCategoryViewSet, basename='ProductCategory')

urlpatterns = [
    path('', include(router.urls)),
    path('shopee_item/', views.post_shopee_item, name='post_shopee_item'),
    path('shopee_item_variations/', views.post_shopee_item_variations, name='post_shopee_item_variations'),
    path('shopee_item_by_category/', ShopeeItemByCategory.as_view())
]
