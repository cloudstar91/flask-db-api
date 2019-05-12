
from src import db
from flask import Flask



class City(db.Model):

    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    city=db.Column(db.String(80),index=True)
    locations = db.relationship('Location', backref='city', lazy=True)

class Location(db.Model):
    __tablename__='location'

    id=db.Column(db.Integer,primary_key=True)
    location=db.Column(db.String(80),index=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'),
        nullable=False)
    
    