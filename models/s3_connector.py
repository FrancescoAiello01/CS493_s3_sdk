import boto3
import os


class S3Connector:
    def __init__(self):
        self.session = None
        self.s3_resource = None
        self.s3_client = None

    def connect(self, aws_profile):
        self.session = boto3.session.Session(profile_name=aws_profile)
        self.s3_resource = self.session.resource('s3')
        self.s3_client = self.session.client('s3')

    def get_buckets(self):
        for bucket in self.s3_resource.buckets.all():
            return bucket.name

    def list_bucket_content(self, bucket_name, directory=''):
        response = self.s3_client.list_objects(Bucket="foobucket", Prefix="")
        contents = []
        for content in response.get('Contents', []):
            contents.append(content.get('Key'))
        return contents

    def upload_file(self, **kwargs):
        with open(kwargs["file_path"], 'rb') as data:
            self.s3_client.upload_fileobj(
                data, kwargs["bucket_name"], kwargs["file_name"])

    def upload_directory(self, **kwargs):
        path = kwargs["directory_path"]
        bucket = self.s3_resource.Bucket(kwargs["bucket_name"])
        aws_directory = kwargs["aws_directory"]

        for sub_directory, directory, files in os.walk(path):
            for file in files:
                full_path = os.path.join(sub_directory, file)
                with open(full_path, 'rb') as data:
                    full_aws_path = aws_directory + \
                        '/' + full_path[len(path)+1:]
                    bucket.put_object(Key=full_aws_path, Body=data)
