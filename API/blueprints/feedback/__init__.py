import random, logging
from blueprints import db
from flask_restful import fields

class Feedbacks(db.Model):
	__tablename__ = "feedback"
	fb_id = db.Column(db.Integer, primary_key = True, autoincrement = True, unique = True)
	user_id = db.Column(db.Integer)
	email = db.Column(db.String(200))
	feedback = db.Column(db.String(1000))

	response_fields = {
		'fb_id':fields.Integer,
		'user_id' : fields.Integer,
		'email':fields.String,
		'feedback':fields.String
	}

	def __init__(self, fb_id, user_id, email, feedback):
		self.fb_id = fb_id
		self.user_id = user_id
		self.email = email
		self.feedback = feedback

	def __repr__(self):
		return '<Feedback %r>' % self.id


