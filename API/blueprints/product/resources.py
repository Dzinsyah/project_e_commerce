# app.py
from flask import Flask, request
import json, logging
from flask_restful import Resource, Api, reqparse, marshal
from logging.handlers import RotatingFileHandler
from flask import Blueprint
from . import * #ngambil init.py
from blueprints import app
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_product= Blueprint('product',__name__)
api = Api(bp_product)


class ProductResources(Resource):
    @jwt_required
    def get(self, product_id=None):
        status_admin = get_jwt_claims()['status_admin']
        if status_admin == 'admin' or status_admin == 'seller':
            if product_id is None:
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default = 1)
                parser.add_argument('rp', type=int, location='args', default = 5)
                parser.add_argument('seller', location='args')
                args = parser.parse_args()

                offset = (args['p']*args['rp'])-args['rp']
            
                qry = Products.query
                if args['seller'] is not None:
                    qry = qry.filter(Products.seller.like("%"+args['seller']+"%"))

                rows = []
                for row in qry.limit(args['rp']).offset(offset).all():
                    rows.append(marshal(row, Products.response_fields))
                return rows, 200, { 'Content-Type': 'application/json' }

            else:
                if status_admin == seller:
                    qry = Products.query.get(product_id)
                #select *from where id = id
                if qry is not None:
                    return marshal(qry, Products.response_fields), 200, { 'Content-Type': 'application/json' }
                return {'status':'NOT FOUND'}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCESS DENIED'}, 404, { 'Content-Type': 'application/json' }

    @jwt_required
    def post(self,product_id = None):
        parser = reqparse.RequestParser()
        parser.add_argument('url_image', location='args')
        parser.add_argument('status', location='args')
        parser.add_argument('vendor', location='args')
        parser.add_argument('name', location='args')
        parser.add_argument('price', location='args')
        parser.add_argument('processor', location='args')
        parser.add_argument('ram', location='args')
        parser.add_argument('memory', location='args')
        parser.add_argument('camera', location='args')
        parser.add_argument('other_description', location='args')
        parser.add_argument('stock', location='args')
        parser.add_argument('location', location='args')
        args = parser.parse_args()

        seller = get_jwt_claims()['username']
        seller_id = get_jwt_claims()['user_id']

        product = Products(None, args['url_image'], seller, args['status'], args['vendor'], args['name'], args['price'], args['processor'], args['ram'], args['memory'], args['camera'], args['other_description'], args['stock'], args['location'], seller_id)
        db.session.add(product)
        db.session.commit()
        return marshal(product, Products.response_fields), 200
# , { 'Content-Type': 'application/json' }

    @jwt_required
    def put(self, product_id=None):
        id = get_jwt_claims()['user_id']
        qry = Products.query.get(product_id)
        if id == qry.seller_id:
            parser = reqparse.RequestParser()
            parser.add_argument('url_image', location='args')
            parser.add_argument('status', location='args')
            parser.add_argument('vendor', location='args')
            parser.add_argument('name', location='args')
            parser.add_argument('price', location='args')
            parser.add_argument('processor', location='args')
            parser.add_argument('ram', location='args')
            parser.add_argument('memory', location='args')
            parser.add_argument('camera', location='args')
            parser.add_argument('other_description', location='args')
            parser.add_argument('stock', location='args')
            parser.add_argument('location', location='args')
            args = parser.parse_args()

            qry = Products.query.get(product_id)
            if qry is not None:
                qry.url_image = args['url_image']
                qry.status = args['status']
                qry.vendor = args['vendor']
                qry.name = args['name']
                qry.price = args['price']
                qry.processor = args['processor']
                qry.ram = args['ram']
                qry.memory = args['memory']
                qry.camera = args['camera']
                qry.other_description = args['other_description']
                qry.stock = args['stock']
                qry.location = args['location']
                db.session.commit()
                return marshal(qry, Products.response_fields), 200, { 'Content-Type': 'application/json' }
            return {'status':'NOT FOUND'}, 404, { 'Content-Type': 'application/json' }
        else:
           return {'status':'ACCES DENIED', 'message':'INVALID USER'}, 404, { 'Content-Type': 'application/json' }

    @jwt_required
    def delete(self, product_id=None):
        status_admin = get_jwt_claims()['status_admin']
        id = get_jwt_claims()['user_id']
        if status_admin == 'admin' or status_admin =='seller':
            id = get_jwt_claims()['user_id']
            qry = Products.query.get(product_id)
            if qry is not None:         
                if id == qry.seller_id:
                    qry = Products.query.get(product_id)
                    db.session.delete(qry)
                    db.session.commit()
                    return "deleted", 200, { 'Content-Type': 'application/json' }
                return {'status':'ACCES DENIED', 'message':'INVALID SELLER'}, 404, { 'Content-Type': 'application/json' }
            return {'status':'NOT FOUND'}, 404, { 'Content-Type': 'application/json' }
        else:
            return {'status':'ACCES DENIED', 'message':'INVALID ADMIN'}, 404, { 'Content-Type': 'application/json' }

api.add_resource(ProductResources,'','/<product_id>')

