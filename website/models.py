#models.py

#imports the database object from this package
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#These id value will be automatically set by the database software when a Note object
#is created.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    data = db.Column(db.String(10000))
    #This uses func to get the current date and time and save it to this variable
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #This foreign key references the id from the User class
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Each User object will have an attribute notes which is a list of all Note 
    # objects related to that user.
    notes = db.relationship('Note')