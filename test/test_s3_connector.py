import unittest
from models.s3_connector import S3Connector

class TestBinarySearchTree(unittest.TestCase):
    """
    Initialization
    """

    def test_instantiation(self):
        """
        A S3 Connector exists
        """
        try:
            S3Connector()
        except NameError:
            self.fail("Could not instantiate S3Connector")