import boto3

class DynamoDBConnector:
    def __init__(self):
        pass
    
    def add_entry(self, **kwargs):
        s3_key = kwargs['directory_name'] # artist/album/name
        genre = kwargs['genre']
        
        