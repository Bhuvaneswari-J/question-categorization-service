from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI, ensure absolute path for consistency
db_path = os.path.join(os.getcwd(), 'exam_types.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence deprecation warning

# Initialize the database connection
db = SQLAlchemy(app)

# Define the ExamType model
class ExamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Define the Subject model
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_type.id'))

# Define the Keyword model
class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

# Root route
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Exam Type API!'}), 200

# Endpoint to add an exam type
@app.route('/exam-type', methods=['POST'])
def add_exam_type():
    data = request.get_json()
    new_exam_type = ExamType(name=data['name'])
    db.session.add(new_exam_type)
    db.session.commit()
    return jsonify({'message': 'Exam type created'}), 201

# Endpoint to add a subject
@app.route('/subject', methods=['POST'])
def add_subject():
    data = request.get_json()
    new_subject = Subject(name=data['name'], exam_type_id=data['exam_type_id'])
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject added'}), 201

# Endpoint to add a keyword
@app.route('/keyword', methods=['POST'])
def add_keyword():
    data = request.get_json()
    new_keyword = Keyword(value=data['value'], subject_id=data['subject_id'])
    db.session.add(new_keyword)
    db.session.commit()
    return jsonify({'message': 'Keyword added'}), 201

if __name__ == '__main__':
    try:
        # Ensure tables are created within app context
        with app.app_context():
            print(f"Creating database tables in: {db_path}")
            db.create_all()
            print("Database tables created successfully in exam_types.db")
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')
