from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for categorization
categories = {
    1: {"category": "Math"},
    2: {"category": "Geography"}
}

@app.route('/categorize/<question_id>', methods=['GET'])
def categorize_question(question_id):
    question_id = int(question_id)
    
    if question_id not in categories:
        return jsonify({'message': 'Question not categorized'}), 404

    return jsonify(categories[question_id]), 200

@app.route('/categorize/<question_id>', methods=['POST'])
def categorize_question_set(question_id):
    data = request.get_json()
    category = data['category']
    
    categories[int(question_id)] = {"category": category}
    return jsonify({'message': 'Question categorized successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
