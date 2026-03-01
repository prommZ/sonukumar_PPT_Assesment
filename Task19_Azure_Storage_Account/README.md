# Task 19 - Azure Storage Account (Blob, File, Table)

## 📌 Objective
To create an Azure Storage Account and explore different storage services including Blob Storage, File Storage, and Table Storage.

This task demonstrates understanding of Azure’s multi-storage services and their practical usage.

---

## 🛠️ Services Used
- Microsoft Azure Portal
- Azure Storage Account
- Blob Storage
- Azure File Storage
- Azure Table Storage

---

## 🖥️ Implementation Steps

### Step 1: Create Storage Account

1. Logged into Azure Portal.
2. Searched for **Storage Accounts**.
3. Clicked **Create**.
4. Configured:
   - Resource Group
   - Storage Account Name (globally unique)
   - Region
   - Performance: Standard
   - Redundancy: LRS (Locally Redundant Storage)
5. Clicked **Review + Create**.
6. Deployment completed successfully.

Storage account status: **Active**

---

## 📦 Part 1: Blob Storage (Object Storage)

### Steps:
1. Opened Storage Account → Containers.
2. Clicked **+ Container**.
3. Entered container name (e.g., `samplecontainer`).
4. Uploaded a sample file (e.g., index.html or text file).

### Result:
File successfully uploaded and accessible inside Blob container.

---

## 📁 Part 2: Azure File Storage

### Steps:
1. Opened Storage Account → File Shares.
2. Clicked **+ File Share**.
3. Entered share name (e.g., `sharedfiles`).
4. Uploaded a sample file.

### Result:
File share created and file stored successfully.

---

## 📊 Part 3: Azure Table Storage

### Steps:
1. Opened Storage Account → Tables.
2. Clicked **+ Table**.
3. Entered table name (e.g., `StudentData`).
4. Added sample entity with:
   - PartitionKey
   - RowKey
   - Name
   - Course

### Result:
Table created and sample data inserted successfully.

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot showing Storage Account overview.
2. Screenshot showing Blob container with uploaded file.
3. Screenshot showing File Share or Table with inserted data.

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Learning

- Azure Storage Account supports multiple storage types.
- Blob Storage is used for object storage (images, files, backups).
- File Storage provides shared file system access.
- Table Storage is a NoSQL key-value storage service.
- Redundancy options improve data durability.

---

## 🎯 Conclusion

In this task, an Azure Storage Account was successfully created and different storage services (Blob, File, and Table) were explored.  
Sample data was uploaded and verified.

This demonstrates understanding of Azure’s multi-storage architecture and practical usage of different storage services.