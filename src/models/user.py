from src import db
from flask_login import UserMixin
from flask import Flask, render_template, flash, redirect, url_for,request


import requests


enrollment= db.Table('enrollment',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('type_id', db.Integer, db.ForeignKey('type.id'))
)    

class User(UserMixin,db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    enrollment = db.relationship('Type', secondary=enrollment, lazy='subquery',
        backref=db.backref('user', lazy=True))

    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

    def check_password(self, password):
      return check_password_hash(self.password_hash, password)

