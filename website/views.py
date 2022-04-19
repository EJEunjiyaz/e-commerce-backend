from rest_framework_mongoengine.viewsets import ModelViewSet

from website.models import ShopeeItem, Store
from website.serializer import ShopeeItemSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = ShopeeItemSerializer


class ShopeeItemViewSet(ModelViewSet):
    queryset = ShopeeItem.objects.all()
    serializer_class = ShopeeItemSerializer
