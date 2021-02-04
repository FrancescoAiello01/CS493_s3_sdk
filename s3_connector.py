import boto3


class S3Connector:
    def __init__(self):
        self.session = None
        self.s3 = None
    
    def connect(self, aws_profile):
        self.session = boto3.session.Session(profile_name=aws_profile)
        self.s3 = self.session.resource('s3')
        
    def print_buckets(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)
            