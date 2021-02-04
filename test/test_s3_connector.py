import unittest
from models.s3_connector import S3Connector

class TestBinarySearchTree(unittest.TestCase):
    """
    Initialization
    """

    def test_instantiation(self):
        """
        An S3 Connector exists
        """
        try:
            S3Connector()
        except NameError:
            self.fail("Could not instantiate S3Connector")
            
            
    def test_instantiation_member_variables(self):
        """
        An S3 Connector should not have a session or s3 upon initialization
        """
        session = None
        s3 = None
        s3_connector = S3Connector()
        self.assertEqual(s3_connector.session, session)
        self.assertEqual(s3_connector.s3, s3)