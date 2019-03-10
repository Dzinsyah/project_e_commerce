import random, logging
from blueprints import db
from flask_restful import fields

class Users(db.Model):
	__tablename__ = "user"
	user_id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
	username = db.Column(db.String(200), unique = True)
	email = db.Column(db.String(100), unique = True)
	password = db.Column(db.String(100))
	address = db.Column(db.String(200))
	telephone = db.Column(db.String(100))
	status_admin = db.Column(db.String(20))

	response_fields = {
		'user_id':fields.Integer,
		'username':fields.String,
		'email':fields.String,
		'password':fields.String,
		'address':fields.String,
		'telephone' :fields.String,
		'status_admin':fields.String
	}

	def __init__(self, user_id, username, email, password, address, telephone, status_admin):
		self.user_id = user_id
		self.username = username 
		self.email = email
		self.password = password
		self.address = address
		self.telephone = telephone
		self.status_admin = status_admin	

	def __repr__(self):
		return '<User %r>' % self.id


