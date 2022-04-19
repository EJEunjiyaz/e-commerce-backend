from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet

from scraper.shopee import shopee_scrape, shopee_scrape_variation
from website.models import ShopeeItem
from website.serializer import ShopeeItemSerializer


@api_view(['POST'])
def post_shopee_item_variations(request):
    url = request.data['url']
    product_name, available_options, variation1, variation2 = shopee_scrape_variation(url)
    # print(product_name, available_options, variation1, variation2)

    json = [
        {
            "name": product_name
        },
        {
            "key": available_options[0],
            "value": variation1
        },
        {
            "key": available_options[1],
            "value": variation2
        }
    ]
    print(json)
    return Response(json)


@api_view(['POST'])
def post_shopee_item(request):
    url = request.data['url']
    print(f"Currently scraping from {url}")
    product_name, product_image, store_name, store_link, store_avatar, variations_list, rating_score, rating_voter, product_sold = shopee_scrape(
        url)

    variations = []
    for variation in variations_list:
        # print("variation", variation)
        options = []
        for key, value in variation.items():
            # print(f"key {key} value {value}")
            option_dict = {"key": key, "value": value}
            options.append(option_dict)
        variations.append(options)
    data = {
        "name": product_name,
        "url": url,
        "image": product_image,
        "store_name": store_name,
        "variations": variations,
        "rating": {
            "avg_star": rating_score,
            "voter": rating_voter
        },
        "sold": product_sold
    }
    # print(data)

    shopee_item_serializer = ShopeeItemSerializer(data=data)
    shopee_item_serializer.is_valid(raise_exception=True)
    shopee_item_serializer.save()
    return Response(shopee_item_serializer.data)


# class StoreViewSet(ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = ShopeeItemSerializer


class ShopeeItemViewSet(ModelViewSet):
    queryset = ShopeeItem.objects.all()
    serializer_class = ShopeeItemSerializer
