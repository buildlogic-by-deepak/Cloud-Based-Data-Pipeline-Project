import json
import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'deepak-crypto-raw-data-2026-001'

def lambda_handler(event, context):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

    current_time = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')

    file_name = f"crypto-data/{current_time}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(data),
        ContentType='application/json'
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Crypto data successfully uploaded to S3")
    }