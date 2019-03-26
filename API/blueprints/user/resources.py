# app.py
from flask import Flask, request
import json, logging
from flask_restful import Resource, Api, reqparse, marshal
from logging.handlers import RotatingFileHandler
from flask import Blueprint
from . import * #ngambil init.py
from blueprints import app
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_user= Blueprint('user',__name__)
api = Api(bp_user)


class UserResources(Resource):
    @jwt_required
    def get(self, user_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin':
            if user_id is None:
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default = 1)
                parser.add_argument('rp', type=int, location='args', default = 5)
                parser.add_argument('username', location='args')
                args = parser.parse_args()

                offset = (args['p']*args['rp'])-args['rp']
            
                qry = Users.query
                if args['username'] is not None:
                    qry = qry.filter_by(name=args['username'])
                    qry = qry.filter(Users.username.like("%"+args['username']+"%"))

                rows = []
                for row in qry.limit(args['rp']).offset(offset).all():
                    rows.append(marshal(row, Users.response_fields))
                return {"message":"success", "status code":200, "user":rows}, 200, { 'Content-Type': 'application/json' }

            else:
                qry = Users.query.get(user_id)
                #select *from where id = id
                if qry is not None:
                    return {"message":"success", "code":200, "user":marshal(qry, Users.response_fields)}, 200, { 'Content-Type': 'application/json' }
                return {"message":"user not found", "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {"message":"ACCESS DENIED, INVALID ADMIN", "code":403}, 403, { 'Content-Type': 'application/json' }

    def post(self,user_id = None):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='args')
        parser.add_argument('email', location='args')
        parser.add_argument('password', location='args')
        parser.add_argument('address', location='args')
        parser.add_argument('telephone', location='args')
        parser.add_argument('status_admin', location='args', default='seller')
        args = parser.parse_args()

        user = Users(None, args['username'], args['email'], args['password'], args['address'], args['telephone'], args['status_admin'])
        db.session.add(user)
        db.session.commit()
        return {"message":"success", "code":200, "user":marshal(user, Users.response_fields)}, 200
# , { 'Content-Type': 'application/json' }
    @jwt_required
    def put(self, user_id=None):
        id = get_jwt_claims()['user_id']
        qry = Users.query.get(user_id)
        if id == qry.user_id:
            parser = reqparse.RequestParser()
            parser.add_argument('username', location='args')
            parser.add_argument('email', location='args')
            parser.add_argument('password', location='args')
            parser.add_argument('address', location='args')
            parser.add_argument('telephone', location='args')
            args = parser.parse_args()
        
            qry = Users.query.get(user_id)
            if qry is not None:
                qry.username = args['username']
                qry.email = args['email']
                qry.password = args['password']
                qry.address = args['address']
                qry.telephone = args['telephone']
                db.session.commit()
                return {"message":"success", "code":200, "user":marshal(qry, Users.response_fields)}, 200, { 'Content-Type': 'application/json' }
            return {'message':'USER NOT FOUND', "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
           return {'status':'ACCES DENIED', 'message':'INVALID USER', "code":403}, 403, { 'Content-Type': 'application/json' }

    @jwt_required
    def delete(self, user_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin':
            qry = Users.query.get(user_id)
            if qry is not None:
                db.session.delete(qry)
                db.session.commit()
                return {"message":"success", "code":200, "status":"deleted"}, 200, { 'Content-Type': 'application/json' }
            return {'message':'USER NOT FOUND', "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCES DENIED', 'message':'INVALID ADMIN', "code":403}, 403, { 'Content-Type': 'application/json' }

api.add_resource(UserResources,'','/<user_id>')
