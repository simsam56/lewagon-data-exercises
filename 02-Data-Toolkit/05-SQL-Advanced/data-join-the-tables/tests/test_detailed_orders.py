# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestDetailedOrders(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_length_results(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, list)

    def test_last_results(self):
        results = self.query_db(self.result.query)
        expected = (20, 'Jim Wood', 'James')
        self.assertEqual(results[len(results) - 1], expected)

    def test_first_results(self):
        results = self.query_db(self.result.query)
        expected = (1, 'Dick Terrcotta', 'James')
        self.assertEqual(results[0], expected)
