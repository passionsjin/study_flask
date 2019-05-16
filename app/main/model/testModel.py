
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt


class TestModel(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "testModel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    testdata = db.Column(db.String(255), unique=True, nullable=False)
    createAt = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Test Model '{}'>".format(self.testdata)
