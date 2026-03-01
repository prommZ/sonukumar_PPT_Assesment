# Task 17 - DynamoDB Table Creation (Basic)

## 📌 Objective
To create a NoSQL table using Amazon DynamoDB and insert sample items.

This task demonstrates basic understanding of serverless database services in AWS.

---

## 🛠️ Services Used
- Amazon DynamoDB
- AWS Management Console

---

## 🖥️ Implementation Steps

### Step 1: Create DynamoDB Table

1. Opened AWS Console → DynamoDB.
2. Clicked **Create Table**.
3. Entered:
   - Table Name: Students
   - Partition Key: StudentID (String)
4. Selected default settings.
5. Clicked **Create Table**.

Table status changed to **Active**.

---

### Step 2: Insert Sample Items

1. Opened the created table.
2. Went to **Explore Table Items**.
3. Clicked **Create Item**.
4. Inserted sample data:

Example Item 1:
- StudentID: 101
- Name: Rahul
- Course: AWS

Example Item 2:
- StudentID: 102
- Name: Anita
- Course: DevOps

5. Saved items successfully.

---

## 📊 Sample Stored Items

| StudentID | Name  | Course |
|-----------|-------|--------|
| 101       | Rahul | AWS    |
| 102       | Anita | DevOps |

Data was successfully inserted into the DynamoDB table.

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot showing DynamoDB table status as **Active**.
2. Screenshot showing inserted items in the table.

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Learning

- DynamoDB is a fully managed NoSQL database.
- It is serverless (no infrastructure management required).
- Uses Partition Key (Primary Key) for data retrieval.
- Highly scalable and low-latency database service.
- Suitable for modern applications requiring high performance.

---

## 🎯 Conclusion

In this task, a DynamoDB table was successfully created and sample items were inserted.  
This demonstrates understanding of basic NoSQL concepts and AWS serverless database services.