# TASK 26 — Azure Global Infrastructure + High Availability

## 🎯 Objective

Deploy highly available Virtual Machine infrastructure using:

- Availability Sets  
- Availability Zones  
- Azure Load Balancer  
- Azure Monitor  
- Storage Account (Diagnostics Logs)  

Verify high availability by simulating VM failure.

---

# 🏗 Architecture Overview

## Azure Global Infrastructure Concept

Azure provides high availability using:

1. Availability Sets (protect from hardware failure)
2. Availability Zones (protect from datacenter failure)
3. Load Balancer (distributes traffic)
4. Azure Monitor (alerting)
5. Storage Account (diagnostics logging)

---

## Architecture Flow

User → Public IP → Load Balancer → Backend Pool → 4 Virtual Machines  

If one VM fails, traffic automatically routes to healthy VMs.

---

# 🛠 Implementation Steps

---

## 🔹 Step 1: Create Resource Group

- Go to Azure Portal → Resource Groups → Create  
- Name: `rg-ha-lab`  
- Region: (Example: East US)  
- Click Review + Create  

---

## 🔹 Step 2: Create Virtual Network

- Go to Virtual Networks → Create  
- Name: `vnet-ha-lab`  
- Address Space: `10.0.0.0/16`  
- Subnet: `10.0.1.0/24`  

---

## 🔹 Step 3: Create Availability Set

- Search Availability Sets → Create  
- Name: `avail-set-1`  
- Fault Domains: 2  
- Update Domains: 5  

---

## 🔹 Step 4: Deploy 2 VMs in Availability Set

Create two VMs:

- `vm-as-1`
- `vm-as-2`

Availability option → Select **Availability Set** → Choose `avail-set-1`  

Allow HTTP (Port 80).

### Install Apache inside each VM

```bash
sudo apt update
sudo apt install apache2 -y
```

Set unique content:

VM 1:
```bash
echo "VM AS 1" | sudo tee /var/www/html/index.html
```

VM 2:
```bash
echo "VM AS 2" | sudo tee /var/www/html/index.html
```

---

## 🔹 Step 5: Deploy 2 VMs in Availability Zones

Create two more VMs:

- `vm-zone-1` → Zone 1  
- `vm-zone-2` → Zone 2  

Availability option → Select **Availability Zone**

Install Apache and set unique content:

```bash
echo "VM Zone 1" | sudo tee /var/www/html/index.html
```

---

## 🔹 Step 6: Create Public Load Balancer

- Search Load Balancers → Create  
- Type: Public  
- SKU: Standard  
- Create new Public IP  
- Create Load Balancer  

---

## 🔹 Step 7: Configure Backend Pool

- Open Load Balancer  
- Go to Backend Pools → Add  
- Add all 4 VMs:
  - vm-as-1
  - vm-as-2
  - vm-zone-1
  - vm-zone-2  

---

## 🔹 Step 8: Configure Health Probe

- Go to Health Probes → Add  
- Protocol: HTTP  
- Port: 80  
- Path: `/`  

---

## 🔹 Step 9: Configure Load Balancing Rule

- Go to Load Balancing Rules → Add  
- Frontend Port: 80  
- Backend Port: 80  
- Associate backend pool  
- Associate health probe  

---

## 🔹 Step 10: Enable Azure Monitor Alert

- Go to Azure Monitor → Alerts → Create Alert Rule  
- Scope: Select VM  
- Condition: CPU Percentage > 70%  
- Create Action Group (Email notification)  
- Create Alert  

---

## 🔹 Step 11: Create Storage Account for Diagnostics

- Go to Storage Accounts → Create  
- Create storage account  
- Open VM → Diagnostic Settings  
- Enable logs  
- Send logs to Storage Account  

---

# 🧪 High Availability Testing

## Test Procedure

1. Open Load Balancer Public IP in browser  
2. Refresh multiple times  
3. Different VM names should appear  

---

## Failure Simulation

1. Stop `vm-as-1`  
2. Refresh browser  
3. Application still accessible  

4. Stop `vm-zone-1`  
5. Application still accessible  

---

## Result

- Traffic automatically routed to healthy VMs  
- Infrastructure remained available  
- High Availability successfully verified  

---

# 📸 Screenshots Required (For Submission)

1. Resource Group Created  
2. Virtual Network Configuration  
3. Availability Set Created  
4. 2 VMs inside Availability Set  
5. 2 VMs in Different Availability Zones  
6. Load Balancer Overview  
7. Backend Pool Configuration  
8. Health Probe Configuration  
9. Load Balancing Rule  
10. Azure Monitor Alert Rule  
11. Storage Account Created  
12. Browser showing Load Balancer Public IP  
13. VM Stopped and Application Still Running  

---

# ✅ Final Outcome

✔ Implemented Availability Set  
✔ Implemented Availability Zones  
✔ Configured Load Balancer  
✔ Enabled Monitoring & Diagnostics  
✔ Verified High Availability under failure  

---

**Task 26 Completed Successfully**