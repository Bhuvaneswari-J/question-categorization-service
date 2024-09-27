from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    exam_year_id = db.Column(db.Integer, nullable=False)
    exam_type_id = db.Column(db.Integer, nullable=False)

@app.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    new_question = Question(text=data['text'], exam_year_id=data['exam_year_id'], exam_type_id=data['exam_type_id'])
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question added'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
