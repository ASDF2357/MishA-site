from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)  # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_from_py.db'  # привязываем базу данных
db = SQLAlchemy(app)  # создаем объект SQLAlchemfrom datetime import datetime


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.user_id} {self.login}'


class Addresses(db.Model):
    address_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    user = db.relationship('Users', backref=db.backref('addresses', lazy=False))
    street = db.Column(db.String(80), nullable=False)
    house = db.Column(db.String(80), nullable=False)
    building = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.address_id} {self.user_id} {self.street} {self.house} {self.building}'


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    user = db.relationship('Users', backref=db.backref('orders', lazy=False))
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.address_id"), nullable=False)
    addresses = db.relationship('Address', backref=db.backref('orders', lazy=False))
    data = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.order_id} {self.user_id} {self.address_id} {self.data} {self.status}'


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.category_id} {self.name}'


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=False)
    category = db.relationship('Categories', backref=db.backref('Products', lazy=False))
    name = db.Column(db.Integer, unique=True, nullable=False)
    about = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.product_id} {self.category_id} {self.address_id} {self.name}'


class Prises(db.Model):
    prise_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    product = db.relationship('Users', backref=db.backref('Orders', lazy=False))
    name = db.Column(db.Integer, unique=True, nullable=False)
    about = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.product_id} {self.category_id} {self.address_id} {self.name}'


db.create_all()


user1 = Users(login="Peter", password="qwe")
user2 = Users(login="Tom", password="qwe")
# st = Streams(number=45, start_date=datetime.now(), course=course)
db.session.add(user1)
db.session.add(user2)

db.session.commit()
