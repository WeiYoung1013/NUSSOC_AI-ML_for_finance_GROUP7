from extends import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'
    user_name = db.Column(db.String(50), primary_key=True)
    user_password = db.Column(db.String(100),nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now())
    
class UserStockSelection(db.Model):
    __tablename__ = 'user_stock_selections'
    login_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), db.ForeignKey('user.user_name'))
    stock_symbol = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship('UserModel', backref=db.backref('stock_selections'))