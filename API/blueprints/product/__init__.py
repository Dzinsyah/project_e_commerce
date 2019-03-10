from blueprints import db
from flask_restful import fields

class Products(db.Model):

    __tablename__ = "Product"
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True) # unique=True
    url_image = db.Column(db.String(255))
    seller = db.Column(db.String(255))
    status = db.Column(db.String(100))
    vendor = db.Column(db.String(100))
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    processor = db.Column(db.String(255))
    ram = db.Column(db.String(255))
    memory = db.Column(db.String(255))
    camera = db.Column(db.String(255))
    other_description = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    location = db.Column(db.String(255))
    seller_id = db.Column(db.Integer)

    # untuk serialize
    response_fields = {
        'product_id': fields.Integer,
        'url_image':fields.String,
        'seller': fields.String,
        'status': fields.String,
        'vendor': fields.String,
        'name': fields.String,
        'price': fields.Integer,
        'processor': fields.String,
        'ram': fields.String,
        'memory': fields.String,
        'camera': fields.String,
        'other_description': fields.String,
        'stock': fields.Integer,
        'location': fields.String,
        'seller_id': fields.Integer
    }

    def __init__(self, product_id, url_image, seller, status, vendor, name, price, processor, ram, memory, camera, other_description, stock, location, seller_id):
        self.product_id = product_id
        self.url_image = url_image
        self.seller = seller
        self.status = status
        self.vendor = vendor
        self.name = name
        self.price = price
        self.processor = processor
        self.ram = ram
        self.memory = memory
        self.camera = camera
        self.other_description = other_description
        self.stock = stock
        self.location = location
        self.seller_id = seller_id

    def __repr__(self): # return dari repr harus string
        return '<Venue %r>' %self.id