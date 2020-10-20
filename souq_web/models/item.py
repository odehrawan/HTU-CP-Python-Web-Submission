from ..core.database import db
from datetime import datetime

class Item(db.Document):
    title = db.StringField()
    description = db.StringField()
    created_at = db.DateTimeField(default=datetime.utcnow())
    item_id = db.StringField()
    task_id = db.StringField()