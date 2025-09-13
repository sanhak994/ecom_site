from flask import Flask, render_template, jsonify, request, session
import os

app = Flask(__name__)
# Use environment variable for secret key with a fallback
app.secret_key = os.environ.get('SECRET_KEY') or os.urandom(24)
# Configure session to be more secure
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('PRODUCTION', 'false').lower() == 'true'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# Initialize shopping cart in session if it doesn't exist
@app.before_request
def before_request():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trending')
def trending():
    return render_template('trending.html')

@app.route('/popular')
def popular():
    return render_template('popular.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/shoes')
def shoes():
    return render_template('shoes.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    item = request.json
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(item)
    session.modified = True
    return jsonify({'success': True, 'cart_count': len(session['cart'])})

@app.route('/cart/count')
def get_cart_count():
    return jsonify({'count': len(session.get('cart', []))})

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    item_id = request.json.get('id')
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['id'] != item_id]
        session.modified = True
    return jsonify({'success': True, 'cart_count': len(session['cart'])})

@app.route('/cart')
def view_cart():
    cart_items = session.get('cart', [])
    total = sum(float(item['price']) for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

if __name__ == '__main__':
    # Get port from environment variable with a fallback to 10000
    port = int(os.environ.get('PORT', 10000))
    # In production, debug should be False
    debug = os.environ.get('PRODUCTION', 'false').lower() != 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
