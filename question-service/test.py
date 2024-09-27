import unittest
import json
from app import app, db, Question

class QuestionServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_question(self):
        response = self.app.post('/question', json={
            'text': 'What is the capital of India?',
            'exam_year_id': 1,
            'exam_type_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Question added', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
