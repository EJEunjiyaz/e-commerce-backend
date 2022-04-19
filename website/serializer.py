from rest_framework_mongoengine import serializers
from mongoengine import *

from website.models import ShopeeItem, OnlyURL


# class StoreSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'


class ShopeeItemSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = ShopeeItem
        fields = '__all__'


class PostShopeeItemSerializer(serializers.DocumentSerializer):
    url = URLField()

    class Meta:
        model = OnlyURL
        fields = ['url']
