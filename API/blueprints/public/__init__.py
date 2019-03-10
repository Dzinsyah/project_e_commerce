import json, logging
from flask import Blueprint, Flask, request
from flask_restful import Api, Resource, reqparse, marshal
from . import *
from blueprints import db, app
from blueprints.product import Products
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import jwt_required, get_jwt_claims


bp_public = Blueprint('public', __name__)
api = Api(bp_public)

class PublicResources(Resource):
    def get(self, product_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default = 1)
        parser.add_argument('rp', type=int, location='args', default = 5)
        parser.add_argument('search', location='args')
        parser.add_argument('orderby', location='args')
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))
        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']
    
        qry = Products.query
        if args['search'] is not None:
            qry = qry.filter(Products.status.like("%"+args['search']+"%"))
            if qry.first() is None:
                qry = Products.query.filter(Products.seller.like("%"+args['search']+"%"))
                if qry.first() is None:
                    qry = Products.query.filter(Products.vendor.like("%"+args['search']+"%"))
                    if qry.first() is None:
                        qry = Products.query.filter(Products.name.like("%"+args['search']+"%"))
                        if qry.first() is None:
                            qry = Products.query.filter(Products.price.like("%"+args['search']+"%"))
                            if qry.first() is None:
                                qry = Products.query.filter(Products.processor.like("%"+args['search']+"%"))
                                if qry.first() is None:
                                    qry = Products.query.filter(Products.ram.like("%"+args['search']+"%"))
                                    if qry.first() is None:
                                        qry = Products.query.filter(Products.memory.like("%"+args['search']+"%"))
                                        if qry.first() is None:
                                            qry = Products.query.filter(Products.camera.like("%"+args['search']+"%"))
                                            if qry.first() is None:
                                                qry = Products.query.filter(Products.location.like("%"+args['search']+"%"))
                                                if qry.first() is None:
                                                    return {'status':'NOT FOUND', 'message':'Product Not Found'}, 404, { 'Content-Type': 'application/json' } 

        if args['orderby']=='price':
            if args['sort']=='desc':
                qry_sorted = qry.order_by(desc(Products.price))
            else:
                qry_sorted = qry.order_by(Products.price)
        else:
            qry_sorted = qry

        rows = []
        for row in qry_sorted.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Products.response_fields))
        return rows, 200, { 'Content-Type': 'application/json' }
api.add_resource(PublicResources,'','')


# def get(self):
#        . . . . 
#        parser.add_argument('orderby', location='args', help='invalid orderby value', choices=('client_id','client_key','status'))
#        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))
#        . . . . 
#        if args['orderby']=='client_id':
#            if args['sort']=='desc':
#                qry_2 = qry_1.order_by(desc(Client.client_id))
#            else:
#                qry_2 = qry_1.order_by(Client.client_id)
#        else:
#            qry_2 = qry_1
#     . . . . 
