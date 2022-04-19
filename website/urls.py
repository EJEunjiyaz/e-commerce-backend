from django.urls import path, include
from rest_framework_mongoengine import routers

from website import views

router = routers.DefaultRouter()
router.register(r'shopee_items', views.ShopeeItemViewSet)
router.register(r'stores', views.StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
