from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Categorization API!'}), 200

# Endpoint to get question text and categorize it based on subject and keywords
@app.route('/categorize/<int:question_id>', methods=['GET'])
def categorize_question(question_id):
    # Fetch the question text from the Question Service
    try:
        response = requests.get(f'http://localhost:5001/question/{question_id}')  # Question Service endpoint
        response.raise_for_status()  # Raise an error for bad responses
        question_data = response.json()
        question_text = question_data['text']
    except requests.exceptions.RequestException as e:
        return jsonify({'message': f'Error fetching question: {str(e)}'}), 500

    # Fetch subjects from the Exam Types Service
    try:
        subjects_response = requests.get('http://localhost:5002/subjects')  # Exam Types Service endpoint for subjects
        subjects_response.raise_for_status()
        subjects = subjects_response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({'message': f'Error fetching subjects: {str(e)}'}), 500

    # Fetch keywords from the Exam Types Service
    try:
        keywords_response = requests.get('http://localhost:5002/keywords')  # Exam Types Service endpoint for keywords
        keywords_response.raise_for_status()
        keywords = keywords_response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({'message': f'Error fetching keywords: {str(e)}'}), 500

    categories = []

    # Categorize question based on subjects and keywords
    for subject in subjects:
        if subject['name'].lower() in question_text.lower():
            category_info = {
                'subject': subject['name'],
                'keywords': []
            }
            # Find related keywords for the matching subject
            related_keywords = [kw for kw in keywords if kw['subject_id'] == subject['id']]
            for keyword in related_keywords:
                if keyword['value'].lower() in question_text.lower():
                    category_info['keywords'].append(keyword['value'])
            categories.append(category_info)

    if not categories:
        return jsonify({'message': 'No categories found for this question'}), 404

    return jsonify({
        'question_id': question_id,
        'question_text': question_text,
        'categories': categories
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
