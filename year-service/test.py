import unittest
import json
from app import app, db, Year

class YearServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_year(self):
        response = self.app.post('/year', json={
            'year_value': '2023'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Year added', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
