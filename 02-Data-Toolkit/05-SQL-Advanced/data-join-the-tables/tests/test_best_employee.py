# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestBestEmployee(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchone()
        return results

    def test_length_results(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 3)

    def test_first_name_in_results(self):
        results = self.query_db(self.result.query)
        self.assertTrue('Patty' in results)

    def test_last_name_in_results(self):
        results = self.query_db(self.result.query)
        self.assertTrue('Lee' in results)

    def test_amount_in_results(self):
        results = self.query_db(self.result.query)
        self.assertTrue(7945.6 in results)

    def test_type_result(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, tuple)
