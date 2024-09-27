from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_types.db'
db = SQLAlchemy(app)

class ExamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_type.id'))

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

@app.route('/exam-type', methods=['POST'])
def add_exam_type():
    data = request.get_json()
    new_exam_type = ExamType(name=data['name'])
    db.session.add(new_exam_type)
    db.session.commit()
    return jsonify({'message': 'Exam type created'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
