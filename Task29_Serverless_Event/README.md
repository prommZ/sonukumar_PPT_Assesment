# TASK 29 — Serverless + Event Driven Architecture (AWS + Azure)

## 🎯 Objective

Implement event-driven serverless architecture using:

- Storage triggers
- Serverless compute
- Managed NoSQL databases
- Logging and monitoring

Cloud Platforms Used:
- AWS
- Azure

---

# 🏗 Architecture Overview

## AWS Flow

S3 Bucket → Lambda Function → DynamoDB → CloudWatch Logs

When a file is uploaded to S3:
- Lambda automatically triggers
- Lambda processes file metadata
- Data stored into DynamoDB
- Logs generated in CloudWatch

---

## Azure Flow

Blob Storage → Azure Function → Cosmos DB

When a file is uploaded to Blob Storage:
- Azure Function triggers automatically
- Data written into Cosmos DB
- Logs available in Monitor

---

# ☁️ PART 1 — AWS Implementation

---

## 🔹 Step 1: Create S3 Bucket

- Go to AWS Console → S3 → Create bucket
- Provide unique bucket name
- Keep default settings
- Create bucket

---

## 🔹 Step 2: Create IAM Role for Lambda

- Go to IAM → Roles → Create Role
- Trusted entity: Lambda
- Attach policies:
  - AWSLambdaBasicExecutionRole
  - AmazonDynamoDBFullAccess
  - AmazonS3ReadOnlyAccess
- Name the role: `lambda-s3-role`

---

## 🔹 Step 3: Create DynamoDB Table

- Go to DynamoDB → Create table
- Table name: `FileUploads`
- Partition key: `fileName` (String)
- Create table

---

## 🔹 Step 4: Create Lambda Function

- Go to Lambda → Create function
- Name: `s3-trigger-function`
- Runtime: Python 3.x
- Execution Role: Use existing role → `lambda-s3-role`

---

## 🔹 Step 5: Add S3 Trigger

- Open Lambda → Add Trigger
- Select S3
- Choose your bucket
- Event Type: PUT (Object Created)
- Save

---

## 🔹 Step 6: Write Lambda Code

Replace default code with:

```python
import json
import boto3
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
```

Deploy function.

---

## 🔹 Step 7: Enable CloudWatch Logs

CloudWatch logs are automatically created.

To verify:
- Go to CloudWatch → Log Groups
- Open log group for Lambda
- Check execution logs

---

## 🧪 AWS Testing

1. Upload a file into S3 bucket
2. Go to DynamoDB → Explore table items
3. Verify file name stored
4. Check CloudWatch logs

---

# ☁️ PART 2 — Azure Implementation

---

## 🔹 Step 6: Create Azure Storage Account

- Azure Portal → Storage Accounts → Create
- Name: `storageeventdemo`
- Create

---

## 🔹 Step 7: Create Azure Function App

- Go to Function App → Create
- Runtime: Python or .NET
- Hosting Plan: Consumption
- Create

---

## 🔹 Step 8: Add Blob Trigger Function

- Inside Function App → Create Function
- Choose Blob Trigger
- Select Storage Account
- Create function

---

## 🔹 Step 9: Create Cosmos DB

- Go to Azure Portal → Cosmos DB → Create
- API: Core (SQL)
- Create database: `FileDB`
- Create container: `Uploads`

---

## 🔹 Step 10: Connect Azure Function to Cosmos DB

Modify Azure Function code to insert data into Cosmos DB.

Example (Python):

```python
import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def main(myblob: func.InputStream):
    logging.info(f"Blob trigger function processed: {myblob.name}")
```

(Configure Cosmos DB connection string in Application Settings.)

---

## 🧪 Azure Testing

1. Upload a file into Blob Storage
2. Go to Cosmos DB → Data Explorer
3. Verify entry created
4. Check Function logs in Monitor

---


## AWS

1. S3 Bucket Created
2. Lambda Function Created
3. S3 Trigger Configured
4. DynamoDB Table
5. CloudWatch Logs
6. DynamoDB item after upload

## Azure

7. Storage Account
8. Function App
9. Blob Trigger
10. Cosmos DB
11. Data Explorer showing entry
12. Function logs after upload

---

# ✅ Final Outcome

✔ Implemented event-driven architecture in AWS  
✔ Implemented event-driven architecture in Azure  
✔ Used serverless compute (Lambda & Azure Function)  
✔ Used managed NoSQL databases (DynamoDB & Cosmos DB)  
✔ Verified trigger-based automatic execution  

---

# 🚀 Conclusion

This project demonstrates:

- Event-driven architecture
- Serverless computing
- Managed database integration
- Monitoring and logging
- Cross-cloud implementation

---

**TASK 29 Completed Successfully**