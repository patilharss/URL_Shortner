from enum import unique
from .extensions import db
from datetime import datetime
import string
from random import choices


# db model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.genrate_short_link()

    def genrate_short_link(self):
        chars = string.digits + string.ascii_letters
        short_url = ''.join(choices(chars, k=3))

        # check in db
        link = self.query.filter_by(short_url=short_url).first()

        # if link exist
        if link:
            return self.genrate_short_link()
        else:
            return short_url
