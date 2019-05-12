from flask import Flask,jsonify,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
# from itsdangerous import URLSafeTimedSerializers
import os
import psycopg2



app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)



convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
} 
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
# ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

from src.models.tutor import Tutor
from src.models.region import City, Location
from src.models.subject import Subject
from src.models.type import Type
from src.models.user import User


@app.route('/')
def list():
    return 'hello' 

@app.route('/tutors',methods=['POST','GET'])
def tutors():
    tutors=Tutor.query.all()
    
    tutors_new=[]
    for tutor in tutors:
        tutors_new.append({"id":tutor.id,"name":tutor.name,"email":tutor.email,"phonenumber":tutor.phonenumber,'rating':tutor.rating,'subject':tutor.subject.subject_name})
    return jsonify(tutors_new)