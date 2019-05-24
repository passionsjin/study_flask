
from .. import db, flask_bcrypt
import datetime
from ..config import key


class Tenants(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "tenants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.String(100), unique=True)
    tenant_id = db.Column(db.String(100), unique=True, nullable=False)
    createAt = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Test Model '{}'>".format(self.testdata)
