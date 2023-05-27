from app import db
from sqlalchemy.sql import func
import pytz
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


UTC = pytz.utc
IST = pytz.timezone('Asia/Ho_Chi_Minh')

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(100), nullable=False)
    notification = db.Column(db.String(1000), nullable=True)
    fb_group = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    

    def set_notification(self, notification):
        self.notification = notification
    
    def set_fb_group(self, fb_group):
        self.fb_group = fb_group

    def __repr__(self):
        return f'<Channel {self.channel_name}>'
    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    description = db.Column(db.String(1000), nullable=True)
    username = db.Column(db.String(100), nullable=False)
    attachments = db.Column(db.String(2000), nullable=True)
    links = db.Column(db.String(2000), nullable=True)
    #tz=IST
    created_at = db.Column(db.DateTime, default=datetime.now())

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index = True, unique = True)
    email = db.Column(db.String(120),index = True,unique = True)
    password = db.Column(db.String(128))

    def  __repr__(self):
        return '<User {}>'.format(self.username)


