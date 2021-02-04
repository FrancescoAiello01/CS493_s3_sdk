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
            
    def list_bucket_content(self, bucket_name, directory=''):
        s3_bucket = self.s3.Bucket(bucket_name)
        return [f.key.split(directory + "/")[0] for f in s3_bucket.objects.filter(Prefix=directory).all()]
            