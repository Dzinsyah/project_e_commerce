import json, sys
from flask import Flask, request, Blueprint
from flask_restful import Resource, Api, reqparse #, abort
from time import strftime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['APP_DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:diar0403@localhost:3306/rest_svc'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bismillah@127.0.0.1:3306/portofolio'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dzinmariadb:bismillah@172.31.37.180/portofolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'NSniSjOIJoijSIjaosJOas'
# app.config['JWI_ACCESS_TOKEN_EXPIRES'] = timedelta(days = 1)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return identity


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


api = Api(app, catch_all_404s=True) #using Api-package from restful



@app.after_request # LOG BISA DILIAT DI TERMINAL!!!!
def after_request(response):
    if request.method == 'GET':
        app.logger.warning("REQUEST_LOG\t%s - %s",
            response.status_code,
            json.dumps({
            'request': request.args.to_dict(),
            'response': json.loads(response.data.decode('utf-8'))
            }))
    else:
        app.logger.warning("REQUEST_LOG\t%s - %s",
            response.status_code,
            json.dumps({
            'request': request.get_json(),
            'response': json.loads(response.data.decode('utf-8'))
            }))
    return response


# from folder.subfolder.namafile import 
# from blueprints.venue.resources import bp_venue
from blueprints.product.resources import bp_product
from blueprints.user.resources import bp_user
from blueprints.login import bp_login
from blueprints.public import bp_public
from blueprints.carts.resources import bp_cart
from blueprints.feedback.resources import bp_feedback
from blueprints.transaction.resources import bp_transaction

# app.register_blueprint(bp_venue, url_prefix = '/venue')
app.register_blueprint(bp_product, url_prefix = '/user/product')
app.register_blueprint(bp_user, url_prefix = '/user/register')
app.register_blueprint(bp_login, url_prefix = '/user/login')
app.register_blueprint(bp_public, url_prefix = '/public/product')
app.register_blueprint(bp_cart, url_prefix = '/user/cart')
app.register_blueprint(bp_feedback, url_prefix = '/user/feedback')
app.register_blueprint(bp_transaction, url_prefix = '/user/transaction')

db.create_all()
