from s3_connector import S3Connector

s3_connector = S3Connector()
s3_connector.connect('s3')
s3_connector.print_bucket("demo-s3-bucket-cs493-2")
