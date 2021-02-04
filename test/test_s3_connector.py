import unittest
import boto3
from moto import mock_s3
from models.s3_connector import S3Connector

class TestS3Connector(unittest.TestCase):
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
        
    
    @mock_s3
    def test_connect_to_aws_s3(self):
        """
        An S3 Connector should successfully connect to aws s3
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')
        
        s3_connector = S3Connector()
        
        try:
            s3_connector.connect("default")
        except:
            self.fail("Could not connect to aws using mock aws s3")
            
    