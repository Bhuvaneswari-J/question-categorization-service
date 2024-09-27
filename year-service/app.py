from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///years.db'
db = SQLAlchemy(app)

class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_value = db.Column(db.String(4), nullable=False)

@app.route('/year', methods=['POST'])
def add_year():
    data = request.get_json()
    new_year = Year(year_value=data['year_value'])
    db.session.add(new_year)
    db.session.commit()
    return jsonify({'message': 'Year added'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
