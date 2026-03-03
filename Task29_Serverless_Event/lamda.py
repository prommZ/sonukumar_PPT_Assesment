import json
import boto3  # type: ignore
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileUploads')

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            file_name = record['s3']['object']['key']
            bucket_name = record['s3']['bucket']['name']
            
            table.put_item(
                Item={
                    'fileName': file_name,
                    'bucketName': bucket_name,
                    'uploadTime': datetime.utcnow().isoformat()
                }
            )
            
        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }