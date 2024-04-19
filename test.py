# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to the Form</h1>', response.data)

    def test_submit_form(self):
        response = self.app.post('/submit', data=dict(name='John', email='john@example.com'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, John! Your email is john@example.com.', response.data)

    def test_submit_form_missing_data(self):
        response = self.app.post('/submit', data=dict(name=''))
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
