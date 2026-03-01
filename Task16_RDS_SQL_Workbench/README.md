# Task 16 - RDS Database + SQL Workbench Connection & Queries

## 📌 Objective
To create a managed relational database using Amazon RDS, connect it using SQL Workbench, and execute basic SQL queries.

This task demonstrates how AWS provides managed database services without handling server maintenance manually.

---

## 🛠️ Services Used
- Amazon RDS (MySQL)
- Amazon EC2 (optional for connectivity testing)
- SQL Workbench / MySQL Workbench

---

## 🖥️ Implementation Steps

### Step 1: Launch RDS Instance

1. Opened AWS Console → RDS.
2. Clicked **Create Database**.
3. Selected:
   - Engine: MySQL
   - Deployment: Free Tier
4. Set:
   - DB Instance Identifier
   - Master Username
   - Password
5. Enabled Public Access (for SQL Workbench connection).
6. Configured Security Group to allow inbound MySQL (Port 3306).
7. Created database.

Status changed to **Available**.

---

### Step 2: Connect Using SQL Workbench

1. Opened SQL Workbench.
2. Entered:
   - Hostname: RDS Endpoint
   - Port: 3306
   - Username
   - Password
3. Tested connection.
4. Successfully connected to RDS database.

---

### Step 3: Execute SQL Queries

### Create Database
```sql
CREATE DATABASE company;
USE company;