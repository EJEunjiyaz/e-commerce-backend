from rest_framework_mongoengine import serializers

from website.models import ShopeeItem, ProductCategory


# class StoreSerializer(serializers.DocumentSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'


class ProductCategorySerializer(serializers.DocumentSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ShopeeItemSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = ShopeeItem
        fields = '__all__'
