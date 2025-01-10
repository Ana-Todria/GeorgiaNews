from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db, login_manager


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    text = db.Column(db.String())
    img = db.Column(db.String())
    link = db.Column(db.String())


class Thing(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    img = db.Column(db.String())
    link = db.Column(db.String())



class New(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    img = db.Column(db.String())
    link = db.Column(db.String())


class Tour(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    img = db.Column(db.String())
    link = db.Column(db.String())


class Info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    text = db.Column(db.String())

class Doc(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    text = db.Column(db.String())


class Bak(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    text = db.Column(db.String())



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String())

    def __init__(self, username, password, role):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
