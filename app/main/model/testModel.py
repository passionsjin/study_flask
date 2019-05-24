
from .. import db, flask_bcrypt
import datetime
from ..config import key


class TestModel(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "testModel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    testdata = db.Column(db.String(255), unique=True, nullable=False)
    createAt = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Test Model '{}'>".format(self.testdata)
