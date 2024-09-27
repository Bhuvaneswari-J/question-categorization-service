from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carts.db'
db = SQLAlchemy(app)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_set = db.Column(db.JSON)

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    new_cart = Cart(user_id=data['user_id'], question_set=data['question_set'])
    db.session.add(new_cart)
    db.session.commit()
    return jsonify({'message': 'Added to cart'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
