from flask import Blueprint, request, session, jsonify
from werkzeug.datastructures import MultiDict
from .forms import Registerform, Loginform
from models import UserModel
from extends import db

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/login", methods=['POST'])
def login():
    form = Loginform(MultiDict(request.json))  # 将JSON数据转换为MultiDict
    if form.validate():
        user_name = form.user_name.data
        user_password = form.password.data
        user = UserModel.query.filter_by(user_name=user_name, user_password=user_password).first()
        if user:
            session['user_name'] = user_name
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    else:
        return jsonify({"errors": form.errors}), 400

@auth.route("/logout", methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logout successful"}), 200

@auth.route("/register", methods=['POST'])
def register():
    user_name=request.json.get('user_name')
    password=request.json.get('password')
    user = UserModel(user_name=user_name, user_password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registration successful"}), 201
