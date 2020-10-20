import mongoengine
from datetime import datetime
from .seller import Seller



 
class Item(mongoengine.Document):
    title = mongoengine.StringField(max_length=200, required=True)
    description = mongoengine.StringField()
    owner_id = mongoengine.StringField()
    is_favorite = mongoengine.BooleanField(default=False)
    created_at = mongoengine.DateTimeField(default=datetime.utcnow())
    item_id = mongoengine.StringField()
    price = mongoengine.StringField()

    meta = {'indexes': [
        {'fields': ['$title', "$description"],
         'default_language': 'english',
         'weights': {'title':10 , 'description':2 }
        }
    ]}

