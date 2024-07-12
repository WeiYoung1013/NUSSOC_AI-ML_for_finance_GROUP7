from flask import Blueprint, redirect, render_template, request, url_for, session
from .forms import Registerform, Loginform
from models import UserModel
from extends import db

auth = Blueprint('auth', __name__ ,url_prefix="/auth")

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        form = Loginform(request.form)
        if form.validate():
            user_name = form.user_name.data
            user_password = form.password.data
            user = UserModel.query.filter_by(user_name=user_name,user_password=user_password).first()
            if user:
                session['user_name'] = user_name
                return redirect("/")
            else:
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))
    else:
        return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@auth.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = Registerform(request.form)
        if form.validate():
            user = UserModel(user_name=form.user_name.data,user_password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))