import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        """Test if the page is loaded correctly."""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_add_item(self):
        """Test adding an item to the application."""
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        response = self.app.get('/')
        self.assertIn(b'Test Item', response.data, "Item not added successfully")

    def test_update_item(self):
        """Test updating an item in the application."""
        self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        response = self.app.post('/update/0', data=dict(new_item="Test Modif"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        response = self.app.get('/')
        self.assertIn(b'Test Modif', response.data, "Item not updated successfully")

    def test_delete_item(self):
        """Test deleting an item from the application."""
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 Found")
        response = self.app.get('/')
        self.assertNotIn(b'Test Item', response.data, "Item not deleted successfully")
        
if __name__ == '__main__':
    unittest.main()