# app.py
from flask import Flask, request, Blueprint
import json, logging
from flask_restful import Resource, Api, reqparse, marshal
from logging.handlers import RotatingFileHandler
# from flask import Blueprint
from . import * #ngambil init.py
from blueprints import app, db
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints.product import Products
from datetime import date, datetime
from sqlalchemy.sql import func


bp_cart = Blueprint('cart', __name__)
api = Api(bp_cart)

class CartResources(Resource):
    @jwt_required
    def get(self, cart_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin'or status_admin =='seller':
            if cart_id is None:
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default = 1)
                parser.add_argument('rp', type=int, location='args', default = 5)
                parser.add_argument('product_name', location='args')
                args = parser.parse_args()

                offset = (args['p']*args['rp'])-args['rp']
                
                #get cart list hanya barang milik seller
                if status_admin == "seller":
                    user_id = get_jwt_claims()['user_id']                 
                    qry = Carts.query.filter_by(user_id=user_id)
                    if args['product_name'] is not None:
                        qry = qry.filter(Carts.product_name.like("%"+args['product_name']+"%"))

                    total_qty = 0
                    total_price = 0
                    for rowss in qry.all():
                        temp = marshal(rowss, Carts.response_fields)
                        total_qty += temp["qty"]
                        total_price += temp["price"]

                    rows = []
                    for row in qry.limit(args['rp']).offset(offset).all():
                        rows.append(marshal(row, Carts.response_fields))
                    return {"message":"success", "code":200, "cartList":rows, "totalQty":total_qty ,"totalPrice":total_price}, 200, { 'Content-Type': 'application/json' }

                #cek semua cart list untuk admin
                qry_admin = Carts.query
                if args['product_name'] is not None:
                    qry_admin = qry_admin.filter(Carts.product_name.like("%"+args['product_name']+"%"))

                rows = []
                for row in qry_admin.limit(args['rp']).offset(offset).all():
                    rows.append(marshal(row, Carts.response_fields))
                return {"message":"success", "code":200, "cartList":rows}, 200, { 'Content-Type': 'application/json' }

            else:
                qry = Carts.query.get(cart_id)
                #select *from where id = id
                if qry is not None:
                    return marshal(qry, Carts.response_fields), 200, { 'Content-Type': 'application/json' }
                return {'status':'NOT FOUND'}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCESS DENIED'}, 404, { 'Content-Type': 'application/json' }
    
    @jwt_required
    def post(self, product_id = None):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', location='args', type=int, required=True)
        parser.add_argument('qty', location='args',type=int, required=True)
        
        args = parser.parse_args()

        product_qry = Products.query.get(args["product_id"])
        if product_qry is None:
            return {"message":"product not found", "code":404},404, { 'Content-Type': 'application/json' }
        
        product_qry.stock -= args["qty"]

        product_json = marshal(product_qry, Products.response_fields)

        if product_json["stock"] < args["qty"]:
            return {"message": "not enough stock on this product", "code":404}, 404, { 'Content-Type': 'application/json' }

        name_product = product_json['name']
        urlimage = product_json['url_image']
        user_id = get_jwt_claims()['user_id']
        harga = product_json["price"] * args["qty"]
        created = datetime.now()
        updated = datetime.now()

        cart = Carts(None, urlimage, args['product_id'], user_id, name_product, args['qty'], harga, created, updated)
        db.session.add(cart)
        db.session.commit()
        return {"message":"success", "code":200, "cartList":marshal(cart, Carts.response_fields)}, 200
# , { 'Content-Type': 'application/json' }

    
    @jwt_required
    def delete(self, cart_id=None):
        status_admin = get_jwt_claims()['status_admin']
        id = get_jwt_claims()['user_id']
        if status_admin == 'admin' or status_admin =="seller":
            qry = Carts.query.get(cart_id)
            id = get_jwt_claims()['user_id']
            if qry is not None:
                if id == qry.user_id:
                    qry = Carts.query.get(cart_id)
                    db.session.delete(qry)
                    db.session.commit()
                    return {"message":"success", "code":200, "status":"deleted"}, 200, { 'Content-Type': 'application/json' }
                return {"message":"invalid user", "code":403}, 403, { 'Content-Type': 'application/json' }
            return {'message':'CART NOT FOUND', "code":404}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCES DENIED', 'message':'INVALID USER', "code":403}, 403, { 'Content-Type': 'application/json' }

api.add_resource(CartResources,'','/<int:cart_id>')
