from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend Running 🚀"

@app.route('/api/products')
def products():
    return jsonify([
        {"name": "Shoes", "price": 999},
        {"name": "Watch", "price": 1499},
        {"name": "Headphones", "price": 1999}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)