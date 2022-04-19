import datetime
import urllib.parse

from mongoengine import *
from decouple import config

username = urllib.parse.quote_plus(config('MONGO_USER'))
password = urllib.parse.quote_plus(config('MONGO_PASSWORD'))
hostname = urllib.parse.quote_plus(config('MONGO_HOST'))
db_name = urllib.parse.quote_plus(config('MONGO_DB'))

connect(host=f"mongodb+srv://{username}:{password}@{hostname}/{db_name}?retryWrites=true&w=majority")


# class Store(Document):
#     name = StringField(primary_key=True)
#     link = URLField()
#     avatar = URLField()


class ShopeeVariation(EmbeddedDocument):
    key = StringField()
    value = StringField()


class ShopeeRating(EmbeddedDocument):
    avg_star = FloatField()
    voter = IntField()


class ShopeeItem(Document):
    name = StringField()
    url = URLField()
    image = URLField()
    store_name = StringField()
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

# store = {
#     "name": "th9320_61347",
#     "link": "https://shopee.co.th/th9320_61347?categoryId=100017&itemId=14938034833",
#     "avatar": "https://cf.shopee.co.th/file/4c8905ef44e0a8686e2354293b5ae418_tn"
# }
#
# item = {
#     "name": "เสื้อเชิ้ตเกาหลี แขนสั้นผู้หญิง สีพื้น ผ้านิ่มนุ่ม เบา ใส่สบาย ไม่ต้องรีดก็ใส่ได้ ผ้าไม่ยับ",
#     "url": "https://shopee.co.th/%E0%B9%80%E0%B8%AA%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B9%89%E0%B8%95%E0%B9%80%E0%B8%81%E0%B8%B2%E0%B8%AB%E0%B8%A5%E0%B8%B5-%E0%B9%81%E0%B8%82%E0%B8%99%E0%B8%AA%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%AB%E0%B8%8D%E0%B8%B4%E0%B8%87-%E0%B8%AA%E0%B8%B5%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B9%88%E0%B8%A1-%E0%B9%80%E0%B8%9A%E0%B8%B2-%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B8%AA%E0%B8%9A%E0%B8%B2%E0%B8%A2-%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B5%E0%B8%94%E0%B8%81%E0%B9%87%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B9%84%E0%B8%94%E0%B9%89-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%A2%E0%B8%B1%E0%B8%9A-i.16489766.14938034833?sp_atk=35102125-2034-40ad-afd7-acc088019733",
#     "image": "https://cf.shopee.co.th/file/077b19603052f16f108dd21ee1dd0d69",
#     "variations": [
#         [
#             {
#                 "key": "สี",
#                 "value": "ขาว"
#             },
#             {
#                 "key": "Size",
#                 "value": "M"
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
#                 "key": "สี",
#                 "value": "ขาว"
#             },
#             {
#                 "key": "Size",
#                 "value": "L"
#             },
#             {
#                 "key": "quantity",
#                 "value": "1"
#             },
#             {
#                 "key": "price",
#                 "value": "145"
#             }
#         ]
#     ],
#     "rating": {
#         "avg_star": "4.7",
#         "voter": 420
#     },
#     "sold": 1700
# }

# store = {
#     "name": "istudiobyspvi",
#     "link": "https://shopee.co.th/istudiobyspvi?categoryId=100013&itemId=7862109494",
#     "avatar": "https://cf.shopee.co.th/file/1268397dcf33d930f6e0485c62b52696_tn"
# }
#
# item = {
#     "name": "Apple iPhone12 หน้าจอ 6.1 นิ้ว",
#     "url": "https://shopee.co.th/Apple-iPhone12-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD-6.1-%E0%B8%99%E0%B8%B4%E0%B9%89%E0%B8%A7-i.287137993.7862109494?sp_atk=095f1cd7-99e1-4671-90d0-12c0d9616fa9",
#     "image": "https://cf.shopee.co.th/file/077b19603052f16f108dd21ee1dd0d69",
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
# istudiobyspvi.save()
# iphone = ShopeeItem(**item, store=istudiobyspvi)
# iphone.save()
