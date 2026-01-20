# pylint: disable-all
# pylint: disable=missing-docstring
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestSpentPerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_type_results(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = self.query_db(self.result.query)
        expected = ('Jim Wood', 1597.9)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = self.query_db(self.result.query)
        expected = ('Toni Faucet', 8700.1)
        self.assertEqual(results[len(results)-1], expected)

    def test_len_resultts(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 5)
