from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configure the database URI, ensure absolute path for consistency
db_path = os.path.join(os.getcwd(), 'users.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence deprecation warning

# Initialize the database connection
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Root route
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the User API!'}), 200

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

# Endpoint to log in a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
    try:
        # Ensure tables are created within app context
        with app.app_context():
            print(f"Creating database tables in: {db_path}")
            db.create_all()
            print("Database tables created successfully in users.db")
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')
