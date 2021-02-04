import boto3


class S3Connector:
    def __init__(self):
        self.session = None
        self.s3 = None
    
    def connect(self, aws_profile):
        self.session = boto3.session.Session(profile_name=aws_profile)
        self.s3 = self.session.resource('s3')
        
    def get_buckets(self):
        for bucket in self.s3.buckets.all():
            return bucket.name
            
    def get_bucket(self, bucket_name):
        bucket = self.s3.Bucket(bucket_name)
        for bucket_object in bucket.objects.all():
            return bucket_object
            