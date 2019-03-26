# app.py
from flask import Flask, request
import json, logging
from flask_restful import Resource, Api, reqparse, marshal
from logging.handlers import RotatingFileHandler
from flask import Blueprint
from . import * #ngambil init.py
from blueprints import app
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_feedback= Blueprint('feedback',__name__)
api = Api(bp_feedback)


class FeedbackResources(Resource):
    @jwt_required
    def get(self, fb_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin':
            if fb_id is None:
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default = 1)
                parser.add_argument('rp', type=int, location='args', default = 5)
                parser.add_argument('email', location='args')
                args = parser.parse_args()

                offset = (args['p']*args['rp'])-args['rp']
            
                qry = Feedbacks.query
                if args['email'] is not None:
                    qry = qry.filter(Feedbacks.email.like("%"+args['email']+"%"))

                rows = []
                for row in qry.limit(args['rp']).offset(offset).all():
                    rows.append(marshal(row, Feedbacks.response_fields))
                return {"message":"success", "status code":200, "feedback":rows}, 200, { 'Content-Type': 'application/json' }

            else:
                qry = Feedbacks.query.get(fb_id)
                #select *from where id = id
                if qry is not None:
                    return {"message":"success", "code":200, "feedback":marshal(qry, Feedbacks.response_fields)}, 200, { 'Content-Type': 'application/json' }
                return {"message":"feedback not found", "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {"message":"ACCESS DENIED, INVALID ADMIN", "code":403}, 403, { 'Content-Type': 'application/json' }

    @jwt_required
    def post(self,fb_id = None):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='args')
        parser.add_argument('feedback', location='args')
        args = parser.parse_args()

        user_id = get_jwt_claims()['user_id']
        
        feedback = Feedbacks(None, user_id, args['email'], args['feedback'])
        db.session.add(feedback)
        db.session.commit()
        return {"message":"success", "code":200, "feedback":marshal(feedback, Feedbacks.response_fields)}, 200
# , { 'Content-Type': 'application/json' }

    @jwt_required
    def delete(self, fb_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin':
            qry = Feedbacks.query.get(fb_id)
            if qry is not None:
                db.session.delete(qry)
                db.session.commit()
                return {"message":"success", "code":200, "status":"deleted"}, 200, { 'Content-Type': 'application/json' }
            return {'message':'FEEDBACK NOT FOUND', "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCES DENIED', 'message':'INVALID ADMIN', "code":403}, 403, { 'Content-Type': 'application/json' }

api.add_resource(FeedbackResources,'','/<fb_id>')
