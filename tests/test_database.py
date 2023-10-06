import unittest

from database import db_engine


class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        try:
            connection = db_engine.connect()
            connection.close()

            self.assertTrue(True, "Database connection successful.")
        except Exception as e:
            self.fail(f"Database connection failed: {str(e)}")


if __name__ == '__main__':
    unittest.main()
