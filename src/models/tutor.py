
from src import db
from flask import Flask


tutorlocation=db.Table('tutorlocation',
    db.Column('tutor_id', db.Integer, db.ForeignKey('tutor.id')),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
)

class Tutor(db.Model):

    __tablename__ = 'tutor'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),index=True)
    email = db.Column(db.String(120), index=True,
                      unique=True,
                      nullable=False)
    phonenumber = db.Column(db.String(80),index=True,
                      unique=True,
                      nullable=False)
    rating = db.Column(db.Float)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
        nullable=False)
    tutorlocation = db.relationship('Location', secondary=tutorlocation, lazy='subquery',
        backref=db.backref('tutor', lazy=True))
    

