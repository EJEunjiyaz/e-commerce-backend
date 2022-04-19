import datetime
import urllib.parse

from mongoengine import *
from decouple import config

username = urllib.parse.quote_plus(config('MONGO_USER'))
password = urllib.parse.quote_plus(config('MONGO_PASSWORD'))
hostname = urllib.parse.quote_plus(config('MONGO_HOST'))
db_name = urllib.parse.quote_plus(config('MONGO_DB'))

connect(host=f"mongodb+srv://{username}:{password}@{hostname}/{db_name}?retryWrites=true&w=majority")


class Store(Document):
    name = StringField()
    link = URLField()
    avatar = URLField()


class ShopeeVariation(EmbeddedDocument):
    key = StringField()
    value = StringField()


class ShopeeRating(EmbeddedDocument):
    avg_star = FloatField()
    voter = IntField()


class ShopeeItem(Document):
    name = StringField(primary_key=True)
    image = URLField()
    store = ReferenceField('Store', reverse_delete_rule=CASCADE)
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)
    variations = ListField(EmbeddedDocumentListField(ShopeeVariation))
    rating = EmbeddedDocumentField(ShopeeRating)
    sold = IntField()

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(ShopeeItem, self).save(*args, **kwargs)


# var = {
#     "name": "Apple iPhone12 หน้าจอ 6.1 นิ้ว",
#     "image": "https://cf.shopee.co.th/file/077b19603052f16f108dd21ee1dd0d69",
#     "store": {
#         "name": "istudiobyspvi",
#         "link": "https://shopee.co.th/istudiobyspvi?categoryId=100013&itemId=7862109494",
#         "avatar": "https://cf.shopee.co.th/file/1268397dcf33d930f6e0485c62b52696_tn"
#     },
#     "created_at": "2022-04-18T05:36:27.084",
#     "variations": [
#         {"Color": "White", "ความจุ": "64GB", "quantity": 0, "price": None},
#         {"Color": "White", "ความจุ": "128GB", "quantity": 0, "price": None},
#         {"Color": "White", "ความจุ": "256GB", "quantity": 0, "price": None},
#         {"Color": "Black", "ความจุ": "64GB", "quantity": 0, "price": None},
#         {"Color": "Black", "ความจุ": "128GB", "quantity": 0, "price": None},
#         {"Color": "Black", "ความจุ": "256GB", "quantity": 0, "price": None},
#         {"Color": "Green", "ความจุ": "64GB", "quantity": 0, "price": None},
#         {"Color": "Green", "ความจุ": "128GB", "quantity": 0, "price": None},
#         {"Color": "Green", "ความจุ": "256GB", "quantity": 0, "price": None},
#         {"Color": "(Product)Red", "ความจุ": "64GB", "quantity": 0, "price": None},
#         {"Color": "(Product)Red", "ความจุ": "128GB", "quantity": 0, "price": None},
#         {"Color": "(Product)Red", "ความจุ": "256GB", "quantity": 0, "price": None}
#     ],
#     "rating": {"avg_star": "4.8", "voter": 1300},
#     "sold": 2500
# }

# store = {
#     "name": "istudiobyspvi",
#     "link": "https://shopee.co.th/istudiobyspvi?categoryId=100013&itemId=7862109494",
#     "avatar": "https://cf.shopee.co.th/file/1268397dcf33d930f6e0485c62b52696_tn"
# }
#
# item = {
#     "name": "Apple iPhone12 หน้าจอ 6.1 นิ้ว",
#     "image": "https://cf.shopee.co.th/file/077b19603052f16f108dd21ee1dd0d69",
#     "store": store,
#     "variations": [
#         [
#             {
#                 "key": "Color",
#                 "value": "White"
#             },
#             {
#                 "key": "ความจุ",
#                 "value": "64GB"
#             },
#             {
#                 "key": "quantity",
#                 "value": "0"
#             },
#             {
#                 "key": "price",
#                 "value": "null"
#             }
#         ],
#         [
#             {
#                 "key": "Color",
#                 "value": "White"
#             },
#             {
#                 "key": "ความจุ",
#                 "value": "128GB"
#             },
#             {
#                 "key": "quantity",
#                 "value": "0"
#             },
#             {
#                 "key": "price",
#                 "value": "null"
#             }
#         ]
#     ],
#     "rating": {
#         "avg_star": "4.8",
#         "voter": 1300
#     },
#     "sold": 2500
# }
#
# istudiobyspvi = Store(**store)
# iphone = ShopeeItem(**item)
# iphone.save()
