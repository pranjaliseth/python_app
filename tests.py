import unittest
from hello import app

class HelloWorldTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up the test client for the Flask app
        self.app = app.test_client()

    def test_hello_world(self):
        # Send a GET request to the root endpoint
        response = self.app.get("/")
        
        # Assert that the response data matches the expected output
        self.assertEqual(response.data, b"<p>Hello, World!</p>")
        
        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
