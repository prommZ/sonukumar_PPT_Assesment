# Task 18 - Azure Virtual Machine (Basic)

## 📌 Objective
To launch and configure a basic Virtual Machine in Microsoft Azure and access it using RDP or SSH.

This task demonstrates understanding of Azure compute services and virtual machine deployment.

---

## 🛠️ Services Used
- Microsoft Azure Portal
- Azure Virtual Machine
- Remote Desktop (RDP) / SSH

---

## 🖥️ Implementation Steps

### Step 1: Create Virtual Machine

1. Logged into Azure Portal.
2. Navigated to **Virtual Machines**.
3. Clicked **Create → Azure Virtual Machine**.
4. Configured:
   - Resource Group
   - VM Name
   - Region
   - Image (Ubuntu / Windows Server)
   - Size (Basic/Free Tier eligible)
5. Set authentication:
   - Username
   - Password (for Windows)
   - SSH Key or Password (for Linux)
6. Allowed inbound ports:
   - RDP (3389) for Windows
   - SSH (22) for Linux
7. Clicked **Review + Create**.
8. Deployment completed successfully.

VM status changed to **Running**.

---

### Step 2: Connect to Virtual Machine

#### For Windows VM:
1. Clicked **Connect → RDP**.
2. Downloaded RDP file.
3. Entered username and password.
4. Successfully accessed Windows desktop.

#### For Linux VM:
1. Clicked **Connect → SSH**.
2. Used command: