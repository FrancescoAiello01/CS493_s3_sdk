import boto3
import os

class DynamoDBConnector:
    def __init__(self):
        self.ddb_client = boto3.client('dynamodb')
    
    def add_entry(self, **kwargs):
        path = kwargs['directory_path']
        genre = kwargs['genre']
        directory_name = kwargs['directory_name']
        
        s3_keys = []
        for sub_directory, directory, files in os.walk(path):
            for file in files:
                full_path = os.path.join(sub_directory, file)
                with open(full_path, 'rb') as data:
                    s3_key = directory_name + \
                        '/' + full_path[len(path)+1:]
                    if '.DS_Store' not in s3_key:
                        s3_keys.append(s3_key)
        
        for key in s3_keys:
            split_key = key.split('/')
            self.batch_write(genre, split_key[0], split_key[1], split_key[2], key)
        
    def batch_write(self, genre, artist, album, song, s3_key):
        self.ddb_client.batch_write_item(
            RequestItems={
                'music': [
                            {
                            'PutRequest': {
                                    'Item': {
                                        'pk': { 'S': f'genre#{genre}' },
                                        'sk': { 'S': f'artist#{artist}' },
                                        'type': { 'S': 'artist'},
                                        'name': { 'S': artist }
                                    },
                                },
                            },
                            {
                                'PutRequest': {
                                    'Item': {
                                        'pk': { 'S': f'artist#{artist}' },
                                        'sk': { 'S': f'album#{album}' },
                                        'type': { 'S': "album" },
                                        'name': { 'S': album }
                                    },
                                },
                            },
                            {
                                'PutRequest': {
                                    'Item': {
                                        'pk': { 'S': f'album#{album}' },
                                        'sk': { 'S': f'song#{song}' },
                                        'type': { 'S': "song" },
                                        'name': { 'S': song },
                                        's3_key': { 'S': s3_key }
                                    },
                                },
                            },  
                        ],
                    }
        )
        