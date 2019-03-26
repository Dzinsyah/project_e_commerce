# app.py
from flask import Flask, request
import json, logging
from flask_restful import Resource, Api, reqparse, marshal
from logging.handlers import RotatingFileHandler
from flask import Blueprint
from . import * #ngambil init.py
from blueprints import app
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints.carts import *
from blueprints.product import *
from datetime import date, datetime

bp_transaction= Blueprint('transaction',__name__)
api = Api(bp_transaction)


class TransactionResources(Resource):
    @jwt_required
    def get(self, tr_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin' or status_admin == 'seller':
            if tr_id is None:
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default = 1)
                parser.add_argument('rp', type=int, location='args', default = 5)
                parser.add_argument('tr_id', location='args')
                args = parser.parse_args()

                offset = (args['p']*args['rp'])-args['rp']          

                if status_admin == "seller":
                    user_id = get_jwt_claims()['user_id']                 
                    qry = Transactions.query.filter_by(user_id=user_id)
                    if args['tr_id'] is not None:
                        qry = qry.filter(Transactions.tr_id.like("%"+args['tr_id']+"%"))

                    rows = []
                    for row in qry.limit(args['rp']).offset(offset).all():
                        rows.append(marshal(row, Transactions.response_fields))
                    return {"message":"success", "code":200, "transaction":rows}, 200, { 'Content-Type': 'application/json' }

                #cek semua transaksi untuk admin
                qry_admin = Transactions.query
                if args['tr_id'] is not None:
                    qry_admin = qry_admin.filter(Transactions.tr_id.like("%"+args['tr_id']+"%"))

                rows = []
                for row in qry_admin.limit(args['rp']).offset(offset).all():
                    rows.append(marshal(row, Transactions.response_fields))
                return {"message":"success", "code":200, "transaction":rows}, 200, { 'Content-Type': 'application/json' }

            else:
                qry = Transactions.query.get(tr_id)
                #select *from where id = id
                if qry is not None:
                    return {"message":"success", "code":200, "transaction":marshal(qry, Transactions.response_fields)}, 200, { 'Content-Type': 'application/json' }
                return {"message":"transaction not found", "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {"message":"ACCESS DENIED, INVALID USER", "code":403}, 403, { 'Content-Type': 'application/json' }

    @jwt_required
    def post(self,tr_id = None):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', location='args')
        parser.add_argument('email', location='args')
        parser.add_argument('address', location='args')
        parser.add_argument('payment_method', location='args')

        args = parser.parse_args()

        user_id = get_jwt_claims()['user_id']
        qry = Carts.query.filter_by(user_id=user_id)

        total_qty = 0
        total_price = 0
        for rowss in qry.all():
            temp = marshal(rowss, Carts.response_fields)
            total_qty += temp["qty"]
            total_price += temp["price"]
        

        status = "waiting for payment"
        created = datetime.now()
        updated = datetime.now()


        transaction = Transactions(None, user_id, args['fullname'], args['email'], args['address'], total_qty, total_price, args['payment_method'], status, created, updated)
        db.session.add(transaction)
        db.session.commit()
        return {"message":"success", "code":200, "transaction":marshal(transaction, Transactions.response_fields)}, 200

    @jwt_required
    def delete(self, tr_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin' or status_admin == 'seller':
            qry = Transactions.query.get(tr_id)
            id = get_jwt_claims()['user_id']
            if qry is not None:
                if id == qry.user_id:
                    db.session.delete(qry)
                    db.session.commit()
                    return {"message":"success", "code":200, "status":"deleted"}, 200, { 'Content-Type': 'application/json' }
                return {'status':'ACCES DENIED', 'message':'INVALID SELLER', "code":403}, 403, { 'Content-Type': 'application/json' }
            return {'message':'TRANSACTION NOT FOUND', "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCES DENIED', 'message':'INVALID USER LOGIN', "code":403}, 403, { 'Content-Type': 'application/json' }

api.add_resource(TransactionResources,'','/<tr_id>')