import unittest
import json
from app import app, db, Category

class CategoryServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_categorize_question(self):
        response = self.app.post('/categorize', json={
            'question_id': 1,
            'subject_id': 1,
            'keyword_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Question categorized', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
