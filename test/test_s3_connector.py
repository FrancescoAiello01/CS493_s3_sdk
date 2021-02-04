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
        s3_resource = None
        s3_client = None
        s3_connector = S3Connector()
        self.assertEqual(s3_connector.session, session)
        self.assertEqual(s3_connector.s3_resource, s3_resource)
        self.assertEqual(s3_connector.s3_client, s3_client)

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
        self.assertEqual(s3_connector.get_buckets(), ["foobucket"])

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
        self.assertEqual(s3_connector.list_bucket_content(
            "foobucket"), ["foofile"])

    @mock_s3
    def test_upload_file_to_s3_bucket(self):
        """
        An S3 Connector should successfully upload a file to specified bucket
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')

        s3_connector = S3Connector()
        s3_connector.connect("default")
        s3_connector.upload_file(
            file_path="test/test_resources/test_file", file_name="foofile", bucket_name="foobucket")

        # get bucket contents
        response = boto3.client('s3').list_objects(Bucket="foobucket")
        contents = []
        for content in response.get('Contents', []):
            contents.append(content.get('Key'))

        self.assertEqual(contents, ["foofile"])

    @mock_s3
    def test_upload_directory_to_s3_bucket(self):
        """
        An S3 Connector should successfully upload a directory of files to a specified bucket
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')

        s3_connector = S3Connector()
        s3_connector.connect("default")
        s3_connector.upload_directory(directory_path="test/test_resources/test_directory",
                                      bucket_name="foobucket", aws_directory="test_directory")

        # get bucket contents
        response = boto3.client('s3').list_objects(Bucket="foobucket")
        contents = []
        for content in response.get('Contents', []):
            contents.append(content.get('Key'))

        self.assertEqual(
            contents, ["test_directory/test_file", "test_directory/test_file2"])

    @mock_s3
    def test_upload_directory_of_directories_to_s3_bucket(self):
        """
        An S3 Connector should successfully upload a directory of directories with files to a specified bucket
        """
        conn = boto3.resource('s3', region_name='us-east-1')
        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket='foobucket')

        s3_connector = S3Connector()
        s3_connector.connect("default")
        s3_connector.upload_directory(directory_path="test/test_resources/test_subdirectory",
                                      bucket_name="foobucket", aws_directory="test_directory")

        # get bucket contents
        response = boto3.client('s3').list_objects(Bucket="foobucket")
        contents = []
        for content in response.get('Contents', []):
            contents.append(content.get('Key'))

        self.assertEqual(
            contents, ["test_directory/sub/fake", "test_directory/sub2/fake"])
