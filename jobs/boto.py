##Please run this to test your Configuration File

import boto3
from config import configuration

s3 = boto3.client(
    's3',
    aws_access_key_id=configuration.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=configuration.get('AWS_SECRET_KEY'),
    region_name=configuration.get('REGION')
)

try:
    response = s3.get_object(Bucket=configuration.get('BUCKET_NAME'), Key='test.json')
    print(response['Body'].read().decode('utf-8'))
except Exception as e:
    print(f"Error accessing S3: {e}")