# TASK 28 — Hybrid Architecture Simulation

## 🎯 Objective

Simulate secure on-prem to cloud architecture using:

- Public & Private Subnets
- Bastion Host (Jump Server)
- Route Tables
- Security Groups
- Controlled SSH access

Verify that private VM is not accessible directly from the internet.

---

# 🏗 Architecture Overview

This project simulates secure hybrid access:

User → Bastion Host (Public Subnet) → Private VM (Private Subnet)

Private VM has:
- No Public IP
- No direct internet access
- SSH allowed only from Bastion

---

# 🛠 Implementation Steps (AWS Version)

---

## 🔹 Step 1: Create VPC with Public & Private Subnets

1. Go to VPC → Create VPC
   - CIDR: 10.0.0.0/16

2. Create Subnets:
   - Public Subnet → 10.0.1.0/24
   - Private Subnet → 10.0.2.0/24

3. Create Internet Gateway (IGW)
   - Attach to VPC

---

## 🔹 Step 2: Configure Route Tables

### Public Route Table
- Add route:
  - 0.0.0.0/0 → Internet Gateway
- Associate with Public Subnet

### Private Route Table
- Do NOT add Internet Gateway route
- Associate with Private Subnet

This isolates private subnet from internet.

---

## 🔹 Step 3: Launch Bastion Host

Launch EC2 instance:

- Name: Bastion-Host
- Subnet: Public Subnet
- Auto-assign Public IP: Enabled
- Security Group:
  - Allow SSH (Port 22) from:
    - Your IP only

---

## 🔹 Step 4: Launch Private VM

Launch EC2 instance:

- Name: Private-Server
- Subnet: Private Subnet
- Auto-assign Public IP: Disabled
- Security Group:
  - Allow SSH (Port 22)
  - Source: Bastion Security Group (NOT 0.0.0.0/0)

This ensures only Bastion can SSH into private VM.

---

## 🔹 Step 5: Configure Security Groups

### Bastion Security Group
- Inbound:
  - SSH (22) → Your Public IP

### Private VM Security Group
- Inbound:
  - SSH (22) → Bastion Security Group

No internet access allowed.

---

## 🔹 Step 6: Access Private VM via Bastion

Step 1: SSH into Bastion

```bash
ssh -i key.pem ec2-user@<Bastion-Public-IP>
```

Step 2: From Bastion, SSH into Private VM

```bash
ssh -i key.pem ec2-user@<Private-VM-Private-IP>
```

Connection successful.

---

## 🔹 Step 7: Verify Private VM Isolation

Try accessing Private VM directly from your laptop:

```bash
ssh -i key.pem ec2-user@<Private-VM-Private-IP>
```

Expected result:

Connection timeout or unreachable

This confirms isolation.

---

# 🌐 Traffic Flow Explanation

1. User connects to Bastion via Internet.
2. Bastion forwards SSH request to Private VM.
3. Private VM responds internally within VPC.
4. No public exposure of private server.

---

# 🔐 Security Benefits

✔ Private VM has no Public IP  
✔ Internet cannot access private subnet  
✔ SSH restricted using Security Group  
✔ Controlled jump-server access  

---

# 📸 Screenshots Required

1. VPC Overview
2. Public & Private Subnets
3. Route Tables Configuration
4. Bastion EC2 Instance
5. Private EC2 Instance
6. Security Group Rules
7. SSH into Bastion
8. SSH from Bastion to Private VM
9. Direct SSH failure to Private VM

---

# 🏁 Final Result

Successfully implemented secure hybrid architecture simulation:

✔ Public Bastion Host  
✔ Private isolated server  
✔ Controlled SSH access  
✔ Verified network isolation  
✔ Documented secure traffic flow  

---

# 📊 Architecture Diagram (Concept)

User  
   ↓  
Internet  
   ↓  
Bastion Host (Public Subnet)  
   ↓  
Private VM (Private Subnet)

---

**TASK 28 Completed Successfully**