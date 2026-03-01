# Task 3 - Attach EBS Volume from Different Availability Zone using Snapshot

## 📌 Objective
To understand how Amazon EBS snapshots work and how to restore a volume in a different Availability Zone (AZ) and attach it to an EC2 instance.

This task demonstrates cross-AZ storage handling using snapshots.

---

## 🛠️ Services Used
- Amazon EC2
- Amazon EBS
- EBS Snapshot

---

## 🖥️ Implementation Steps

### Step 1: Create EBS Volume
1. Created an EC2 instance in Availability Zone A.
2. Created and attached an EBS volume to the instance.
3. Formatted and mounted the volume.
4. Added sample data inside the volume.
![alt text](all-vol-us-east-1a.png)
---

### Step 2: Create Snapshot
1. Went to EC2 Dashboard → Volumes.
2. Selected the attached volume.
3. Clicked on **Create Snapshot**.
4. Snapshot was created successfully.
![alt text](snapshots-vol.png)
---

### Step 3: Create Volume in Different AZ
1. Opened Snapshots section.
2. Selected created snapshot.
3. Clicked **Create Volume**.
4. Selected a different Availability Zone (AZ C).
5. Created new volume.
![alt text](all-vol-us-east-1c.png)
---

### Step 4: Attach Volume to EC2
1. Launched new EC2 instance in AZ C.
2. Attached the newly created volume.
3. Mounted the volume:
![alt text](instance-us-east-1c.png)