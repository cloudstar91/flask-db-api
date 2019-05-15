
from src import db
from flask import Flask


class TutorLocation(db.Model):
    __tablename__='tutorlocation'
    id = db.Column(db.Integer,primary_key=True)
    tutor_id=db.Column(db.Integer,db.ForeignKey('tutor.id'))
    location_id=db.Column(db.Integer,db.ForeignKey('location.id')) 

    def __init__(self,tutor_id,location_id):
        self.tutor_id=tutor_id
        self.location_id=location_id
   
        
 

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
    hourlyrate=db.Column(db.Integer,nullable=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
        nullable=False)

    locations = db.relationship('Location', secondary='tutorlocation', lazy='subquery',
        backref=db.backref('tutors', lazy=True))



    

