from main import app
import unittest


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_page_data(self):
        response = self.app.get('/hello')
        self.assertEqual(response.data.decode('utf-8'), 'Hello everyone!!')


if __name__ == '__main__':
    unittest.main()
