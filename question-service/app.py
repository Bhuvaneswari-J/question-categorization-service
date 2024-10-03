from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI, ensure absolute path for consistency
db_path = os.path.join(os.getcwd(), 'questions.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence deprecation warning

# Initialize the database connection
db = SQLAlchemy(app)

# Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    exam_year_id = db.Column(db.Integer, nullable=False)
    exam_type_id = db.Column(db.Integer, nullable=False)

# Root route
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Question API!'}), 200

# Endpoint to add a question
@app.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    new_question = Question(
        text=data['text'],
        exam_year_id=data['exam_year_id'],
        exam_type_id=data['exam_type_id']
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question added'}), 201

if __name__ == '__main__':
    try:
        # Ensure tables are created within app context
        with app.app_context():
            print(f"Creating database tables in: {db_path}")
            db.create_all()
            print("Database tables created successfully in questions.db")
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')
