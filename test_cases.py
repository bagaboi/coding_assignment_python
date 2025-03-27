import unittest
import json
from app import app  # My Flask app is in app.py

class Tester(unittest.TestCase):

    def setUp(self):
        # Seting up for test methods.
        self.app = app.test_client()
        self.app.testing = True

    def test_valid(self):
        # Test with a valid pangram string.
        data = {"text": "abcdefghijklmnopqrstuvwxyz"}
        response = self.app.post('/check_string_alphabets', json=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['result'], True)

    def test_valid_case_insensitive(self):
        # Test with a valid pangram string with mixed case.
        data = {"text": "abcdefghijklMNopqrstuvwxyz"}
        response = self.app.post('/check_string_alphabets', json=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['result'], True)

    def test_valid_with_extra_characters(self):
        # Test with a valid pangram string containing numbers and symbols.
        data = {"text": "abcdefghijklmnopqrstuvwxyz!.3424abcd"}
        response = self.app.post('/check_string_alphabets', json=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['result'], True)

    def test_invalid_missing_letters(self):
        # Test with a string missing some letters of the alphabet.
        data = {"text": "Hello world"}
        response = self.app.post('/check_string_alphabets', json=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['result'], False)

    def test_empty_string(self):
        # Test with an empty string.
        data = {"text": ""}
        response = self.app.post('/check_string_alphabets', json=data)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response_data['result'], False)


    def test_invalid_json_payload(self):
        # Test with an invalid JSON payload.
        response = self.app.post('/check_string_alphabets', data='{"text": "hello"', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', response_data)

if __name__ == '__main__':
    unittest.main()
