import os
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        # Define your database connection URL here
        root = os.getcwd()
        self.database_absolute_path = os.path.join(root, "../database/db.sqlite")
        self.database_url = f"sqlite:///{self.database_absolute_path}"

    def test_database_connection(self):
        try:
            # Attempt to create a database engine and establish a connection
            engine = create_engine(self.database_url)
            connection = engine.connect()
            connection.close()

            # If the connection was successful, the test should pass
            self.assertTrue(True, "Database connection successful.")
        except Exception as e:
            # If there was an exception, the test should fail with an error message
            self.fail(f"Database connection failed: {str(e)}")


if __name__ == '__main__':
    unittest.main()
