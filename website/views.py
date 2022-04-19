from rest_framework_mongoengine.viewsets import ModelViewSet

from website.models import ShopeeItem
from website.serializer import ShopeeItemSerializer


class ShopeeItemViewSet(ModelViewSet):
    queryset = ShopeeItem.objects.all()
    serializer_class = ShopeeItemSerializer
