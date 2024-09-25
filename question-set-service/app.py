from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for question sets
question_sets = {
    "exam_type_1": [{"id": 1, "question": "What is 2 + 2?"}],
    "exam_type_2": [{"id": 1, "question": "What is the capital of France?"}],
}

@app.route('/questions/<exam_type>', methods=['GET'])
def get_questions(exam_type):
    if exam_type not in question_sets:
        return jsonify({'message': 'Exam type not found'}), 404

    return jsonify(question_sets[exam_type]), 200

@app.route('/questions/<exam_type>', methods=['POST'])
def add_question_set(exam_type):
    data = request.get_json()
    question = data['question']

    if exam_type not in question_sets:
        question_sets[exam_type] = []

    question_sets[exam_type].append({"id": len(question_sets[exam_type]) + 1, "question": question})
    return jsonify({'message': 'Question set added!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
