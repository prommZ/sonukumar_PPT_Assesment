# TASK 27 — IAM & Access Control (AWS + Azure)

## 🎯 Objective

Implement access control and role-based permissions in:

- AWS (IAM Users, Roles, Policies)
- Azure (Microsoft Entra ID + RBAC)

Verify allowed and restricted actions.

---

# ☁️ PART 1 — AWS IAM Implementation

---

## 🔹 Step 1: Create IAM User

1. Go to AWS Console → IAM → Users
2. Click Create User
3. User name: Developer
4. Enable:
   - AWS Management Console access
5. Create user

---

## 🔹 Step 2: Attach EC2 Full Access Policy

1. During permission setup
2. Attach policy:
   - AmazonEC2FullAccess
3. Complete user creation

This allows full EC2 access.

---

## 🔹 Step 3: Create Custom Policy to Deny S3 Delete

1. Go to IAM → Policies → Create Policy
2. Select JSON
3. Paste the following:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "s3:DeleteObject",
      "Resource": "*"
    }
  ]
}
```

4. Name policy:
   - DenyS3DeletePolicy
5. Create policy

---

## 🔹 Step 4: Attach Policy via IAM Role

1. Go to IAM → Roles → Create Role
2. Trusted entity: AWS Service → EC2
3. Attach:
   - DenyS3DeletePolicy
4. Create role

Attach this role to EC2 instance.

OR  
You can attach DenyS3DeletePolicy directly to the Developer user.

---

## 🔹 Step 5: Testing AWS Permissions

Login as Developer user.

### ✅ Test EC2

- Launch EC2 instance → Should work

### ❌ Test S3 Delete

1. Go to S3
2. Upload file
3. Try to delete file

Expected result:
Access Denied error

---

# ☁️ PART 2 — Azure RBAC Implementation

---

## 🔹 Step 6: Go to Microsoft Entra ID

1. Open Azure Portal
2. Search Microsoft Entra ID
3. Open Users

---

## 🔹 Step 7: Create New User

1. Click New User
2. Username: developer@yourdomain.onmicrosoft.com
3. Set password
4. Create

---

## 🔹 Step 8: Assign Reader Role on Resource Group

1. Go to Resource Group
2. Click Access Control (IAM)
3. Click Add → Add role assignment
4. Select Role:
   - Reader
5. Assign to:
   - Created user

This gives read-only access to entire Resource Group.

---

## 🔹 Step 9: Assign Contributor Role on Specific VM

1. Open specific Virtual Machine
2. Go to Access Control (IAM)
3. Add Role Assignment
4. Select:
   - Contributor
5. Assign to created user

Now user can modify that VM only.

---

## 🔹 Step 10: Testing Azure Permissions

Login as new Entra ID user.

### ✅ Allowed Actions

- Can Start/Stop assigned VM
- Can Modify assigned VM
- Can View Resource Group resources

### ❌ Restricted Actions

- Cannot create new resources in Resource Group
- Cannot delete other VMs
- Cannot modify other resources

---

# 📸 Screenshots Required

## AWS

1. IAM User Created
2. EC2 Full Access Policy Attached
3. Custom Deny Policy JSON
4. Role Created
5. EC2 Launch Success
6. S3 Delete Access Denied Error

## Azure

7. Entra ID User Created
8. Reader Role Assignment
9. Contributor Role on VM
10. Successful VM Action
11. Permission Denied Example

---

# ✅ Final Outcome

✔ Implemented IAM user with controlled access in AWS  
✔ Enforced explicit Deny for S3 delete  
✔ Implemented RBAC in Azure  
✔ Assigned role at resource group level  
✔ Assigned role at individual VM level  
✔ Successfully demonstrated allowed and restricted actions  

---

**TASK 27 Completed Successfully**