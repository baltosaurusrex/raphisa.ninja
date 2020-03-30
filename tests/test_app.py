import os
import unittest

import raphisaninja as app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """Initial test: Ensure flask was set up correctly."""
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """Initial test: Ensure that the database exists."""
        tester = os.path.exists("flaskr.db")
        self.assertEqual(tester, True)
