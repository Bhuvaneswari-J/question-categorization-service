import unittest
import json
from app import app, db, Cart

class CartServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_to_cart(self):
        response = self.app.post('/cart', json={
            'user_id': 1,
            'question_set': [
                {'question_id': 1, 'subject_id': 1, 'keyword_id': 1},
                {'question_id': 2, 'subject_id': 2, 'keyword_id': 2}
            ]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Added to cart', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
