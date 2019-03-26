import random, logging
from blueprints import db
from flask_restful import fields

class Carts(db.Model):
	__tablename__ = "cart"
	cart_id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
	urlimage = db.Column(db.String(200))
	product_id = db.Column(db.Integer)
	user_id = db.Column(db.Integer)
	product_name = db.Column(db.String(200))
	qty = db.Column(db.Integer)
	price = db.Column(db.Integer)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)

	response_fields = {
		'cart_id':fields.Integer,
		'urlimage':fields.String,
		'product_id':fields.Integer,
		'user_id':fields.String,
		'product_name':fields.String,
		'qty':fields.Integer,
		'price':fields.Integer,
		'created_at' :fields.DateTime,
		'updated_at':fields.DateTime
	}

	response_price ={
		'price':fields.Integer
	}

	def __init__(self, cart_id, urlimage, product_id, user_id, product_name, qty, price, created_at, updated_at):
		self.cart_id = cart_id
		self.urlimage = urlimage
		self.product_id = product_id 
		self.user_id = user_id
		self.product_name = product_name
		self.qty = qty
		self.price = price
		self.created_at = created_at
		self.updated_at = updated_at	

	def __repr__(self):
		return '<Cart %r>' % self.id


