from main import app
import unittest


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_page_data(self):
        response = self.app.get('/')
        response1 = self.app.get('/index')
        self.assertEqual(response.data.decode('utf-8'), 'This is our home page')
        self.assertEqual(response.data.decode('utf-8'), response.data.decode('utf-8'))
        self.assertEqual(response1.data.decode('utf-8'), 'This is our home page')

    def test_other_page_data(self):
        response = self.app.get('/vamsi')
        self.assertEqual(response.data.decode('utf-8'), "hello vamsi")

    def test_other_page_response_code(self):
        response = self.app.get('/vasu')
        self.assertEqual(response.status_code, 200)

    def test_non_existent_page_response_code(self):
        response = self.app.get('/index/nonexistentpage')
        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()