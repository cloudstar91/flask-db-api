from src import db
from flask import Flask



class Type(db.Model):

    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String,nullable=False)



    # city=db.Column(db.String(80),index=True)
    # location= events = db.relationship('Location', backref='city', lazy=True)