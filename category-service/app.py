from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///categories.db'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, nullable=False)
    subject_id = db.Column(db.Integer, nullable=False)
    keyword_id = db.Column(db.Integer, nullable=False)

@app.route('/categorize', methods=['POST'])
def categorize():
    data = request.get_json()
    new_category = Category(question_id=data['question_id'], subject_id=data['subject_id'], keyword_id=data['keyword_id'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Question categorized'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
