from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database URI, ensure absolute path for consistency
db_path = os.path.join(os.getcwd(), 'years.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence deprecation warning

# Initialize the database connection
db = SQLAlchemy(app)

# Define the Year model
class Year(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_value = db.Column(db.String(4), nullable=False)

# Root route
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Year API!'}), 200

# Endpoint to add a year
@app.route('/year', methods=['POST'])
def add_year():
    data = request.get_json()
    new_year = Year(year_value=data['year_value'])
    db.session.add(new_year)
    db.session.commit()
    return jsonify({'message': 'Year added'}), 201

if __name__ == '__main__':
    try:
        # Ensure tables are created within app context
        with app.app_context():
            print(f"Creating database tables in: {db_path}")
            db.create_all()
            print("Database tables created successfully in years.db")
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')
