import random, logging
from blueprints import db
from flask_restful import fields

class Transactions(db.Model):
	__tablename__ = "transaction"
	tr_id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
	user_id = db.Column(db.Integer)
	fullname = db.Column(db.String(200))
	email = db.Column(db.String(200))
	address = db.Column(db.String(1000))
	total_qty = db.Column(db.Integer)
	total_price = db.Column(db.Integer)
	payment_method = db.Column(db.String(200))
	status = db.Column(db.String(200))
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, nullable=False)

	response_fields = {
		'tr_id':fields.Integer,
		'user_id' : fields.Integer,
		'fullname': fields.String,
		'email':fields.String,
		'address':fields.String,
		'total_qty':fields.Integer,
		'total_price':fields.Integer,
		'payment_method':fields.String,
		'status':fields.String,
		'created_at' :fields.DateTime,
		'updated_at':fields.DateTime
	}

	def __init__(self, tr_id, user_id, fullname, email, address, total_qty, total_price, payment_method, status, created_at, updated_at):
		self.tr_id = tr_id
		self.user_id = user_id
		self.fullname = fullname
		self.email = email
		self.address = address
		self.total_qty = total_qty
		self.total_price = total_price
		self.payment_method = payment_method
		self.status = status
		self.created_at = created_at
		self.updated_at = updated_at

	def __repr__(self):
		return '<Transaction %r>' % self.id


