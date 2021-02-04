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
            
    
    @mock_s3
    def test_get_buckets(self):
        """
        An S3 Connector should successfully get s3 bucket names
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')
        
        s3_connector = S3Connector()
        s3_connector.connect("default")
        self.assertEqual(s3_connector.get_buckets(), "foobucket")
        
        
    @mock_s3
    def test_list_bucket_content(self):
        """
        An S3 Connector should successfully list s3 bucket contents
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')
        # Upload fake file to bucket
        s3 = boto3.client('s3')
        with open('test/test_resources/test_file', 'rb') as data:
            s3.upload_fileobj(data, 'foobucket', 'foofile')
        
        s3_connector = S3Connector()
        s3_connector.connect("default")
        self.assertEqual(s3_connector.list_bucket_content("foobucket"), ["foofile"])
        
        