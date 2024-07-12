from extends import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.String(50), primary_key=True)
    user_password = db.Column(db.String(100),nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now())