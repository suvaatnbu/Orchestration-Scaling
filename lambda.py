import json
import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    backup_data = "Sample MongoDB backup data"
    file_name = f"mongodb-backup-{timestamp}.txt"
    
    s3.put_object(Bucket='your-s3-bucket-name', Key=file_name, Body=backup_data)
    return {
        'statusCode': 200,
        'body': json.dumps('Backup successful!')
    }

