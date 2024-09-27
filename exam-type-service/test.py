import unittest
import json
from app import app, db, ExamType

class ExamTypeServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_exam_type(self):
        response = self.app.post('/exam-type', json={
            'name': 'UPSC'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Exam type created', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
