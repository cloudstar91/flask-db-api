from flask import Flask,jsonify,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
# from itsdangerous import URLSafeTimedSerializers
import os
import psycopg2
from flask_cors import CORS





app = Flask(__name__)
CORS(app)
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

from src.models.tutor import Tutor, TutorLocation
from src.models.region import City, Location
from src.models.subject import Subject
from src.models.type import Type
from src.models.user import User


@app.route('/')
def list():
    return 'hello' 

@app.route('/tutors',methods=['POST','GET'])
def tutors():
    
    location_id = request.args['location']
    subject_id = request.args['subject']
    
    tutors=Tutor.query.join(TutorLocation).filter(TutorLocation.location_id == location_id,Tutor.subject_id==subject_id).all()
    if len(tutors)>0:
        tutors_new=[]
        location_arr=[]
        for tutor in tutors:
            for location in tutor.locations:
                location_arr.append({"id":location.id})
            tutors_new.append({"success":True,"id":tutor.id,"name":tutor.name,"email":tutor.email,"phonenumber":tutor.phonenumber,'subject':tutor.subject.subject_name,'hourly_rate':tutor.hourlyrate,'location':location_arr})
        return jsonify(tutors_new)
    elif len(tutors)==0:
        return jsonify({"success":False})
    

@app.route('/login',methods=['POST'])
def login():
    if request.method =='POST':
        data=request.get_json()
        user=User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({'isLogin':True,'current_user':user.username,'message':'welcome back'})
        else:   
            return jsonify({'isLogin':False,'message':'wrong'})
    return redirect("http://localhost:5000")


@app.route('/city',methods=['POST','GET'])
def city():
    cities=City.query.all()
    city_arr=[]
    for city in cities:
        city_arr.append({"id":city.id,"name":city.city})
    return jsonify(city_arr)

@app.route('/location',methods=['POST','GET'])
def location():
    locations=Location.query.order_by(Location.location).all()
    
    location_arr=[]
    for location in locations:
        location_arr.append({"id":location.id,"name":location.location,"city_id":location.city.id})
    return jsonify(location_arr)


@app.route('/subject',methods=['POST','GET'])
def subject():
    subjects=Subject.query.all()
    subject_arr=[]
    for subject in subjects:
        subject_arr.append({"id":subject.id,  "name":subject.subject_name})
    return jsonify(subject_arr)

@app.route('/signup',methods=['POST'])
def signup():
    if request.method =='POST':
        data=request.get_json()
        users=User.query.filter_by(email=data['email']).first()
        users2=User.query.filter_by(username=data['username']).first()
        if users or users2:
            return jsonify({'success':False})
        else:
            user=User(username=data['username'],email=data['email'])
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'success':True,'username':user.username})
    return redirect("http://localhost:5000")