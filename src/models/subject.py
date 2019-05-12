from src import db
from flask import Flask



subjectlocation=db.Table('subjectlocation',
    db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
)    

class Subject(db.Model):

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    subject_name=db.Column(db.String(120),nullable=False)
    tutor_id = db.relationship('Tutor', backref='subject', lazy=True)
    subjectlocation = db.relationship('Location', secondary=subjectlocation, lazy='subquery',
        backref=db.backref('subject', lazy=True))



    
