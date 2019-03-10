from e_commerce_project import app
from flask import render_template

@app.route('/base')
def index():
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listproduct')
def listproduct():
    return render_template('list_product.html')

@app.route('/search')
def search():
    return render_template('search_result.html')

@app.route('/productdetail')
def productdetail():
    return render_template('product_detail.html')

@app.route('/signin')
def signin():
    return render_template('sign_in.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about_us.html')
    
@app.route('/contactus')
def contactus():
    return render_template('contact_us.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/addProduct')
def addproduct():
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug = True)