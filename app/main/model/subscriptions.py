
from .. import db, flask_bcrypt
from sqlalchemy.dialects.mysql import JSON
import datetime
from ..config import key
import enum


class Subscriptions(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "Subscriptions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tenant_id = db.Column(db.String(100), unique=True)
    subscription_id = db.Column(db.String(100), unique=True, nullable=False)
    product_type = db.Column(db.Enum(ProductType))
    service_list = db.Column(JSON)
    createAt = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Test Model '{}'>".format(self.testdata)


class ProductType(enum.Enum):
    Azure = "Azure"
    O365 = "o365"