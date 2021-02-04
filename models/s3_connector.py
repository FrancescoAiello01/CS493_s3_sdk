import boto3


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
        response = self.s3_client.list_objects(Bucket="foobucket")
        contents = []
        for content in response.get('Contents', []):
            contents.append(content.get('Key'))
        return contents
            
            
    def upload_file(self, **kwargs):
        with open(kwargs["file_path"], 'rb') as data:
            self.s3_client.upload_fileobj(data, kwargs["bucket_name"], kwargs["file_name"])
            