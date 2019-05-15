from src import db
from flask import Flask


class SubjectLocation(db.Model):

    __tablename__='subjectlocation'
    id = db.Column(db.Integer,primary_key=True)
    subject_id= db.Column(db.Integer, db.ForeignKey('subject.id'))
    location_id=db.Column(db.Integer, db.ForeignKey('location.id'))

    def __init__(self,subject_id,location_id):
        self.subject_id=subject_id
        self.location_id=location_id


class Subject(db.Model):

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    subject_name=db.Column(db.String(120),nullable=False)
    tutor_id = db.relationship('Tutor', backref='subject', lazy=True)
    locations = db.relationship('Location', secondary='subjectlocation', lazy='subquery',
        backref=db.backref('subjects', lazy=True))


    
