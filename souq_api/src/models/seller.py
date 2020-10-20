import mongoengine 
from datetime import datetime


class Seller(mongoengine.Document):
    title = mongoengine.StringField()
    description = mongoengine.StringField()
    price = mongoengine.StringField()
    category = mongoengine.StringField()
    seller_id = mongoengine.StringField()

    owner_id = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
