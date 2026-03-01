# Task 20 - Azure VNet (Basic Networking Practical)

## 📌 Objective
To configure a Virtual Network (VNet), create subnets, and apply Network Security Group (NSG) rules in Microsoft Azure.

This task demonstrates the fundamentals of cloud networking in Azure.

---

## 🛠️ Services Used
- Microsoft Azure Portal
- Azure Virtual Network (VNet)
- Subnets
- Network Security Group (NSG)

---

## 🌐 Implementation Steps

### Step 1: Create Virtual Network (VNet)

1. Logged into Azure Portal.
2. Searched for **Virtual Networks**.
3. Clicked **Create**.
4. Configured:
   - Resource Group
   - VNet Name
   - Region
   - Address Space (e.g., 10.0.0.0/16)
5. Created default subnet (e.g., 10.0.1.0/24).
6. Clicked **Review + Create**.
7. Deployment completed successfully.

---

### Step 2: Create Additional Subnet

1. Opened the created VNet.
2. Navigated to **Subnets**.
3. Clicked **+ Subnet**.
4. Added:
   - Subnet Name (e.g., Subnet-2)
   - Address Range (e.g., 10.0.2.0/24)
5. Saved configuration.

---

### Step 3: Configure Network Security Group (NSG)

1. Created a new **Network Security Group**.
2. Added inbound rule:
   - Allow SSH (Port 22) or RDP (Port 3389)
   - Source: Any
   - Action: Allow
3. Associated NSG with subnet or VM network interface.

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot showing VNet with address space and subnets.
2. Screenshot showing NSG inbound rule configuration.

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Learning

- VNet is the foundation of Azure networking.
- Subnets divide the network into smaller segments.
- NSG controls inbound and outbound traffic.
- CIDR notation defines IP address ranges.
- Similar concept to AWS VPC.

---

## 🎯 Conclusion

In this task, a Virtual Network was successfully created with multiple subnets and security rules using NSG.  
This demonstrates understanding of Azure networking fundamentals and cloud-based network segmentation.

The objective of learning basic networking in Azure was successfully achieved.