# Task 14 - CloudWatch Alarm (70% CPU → Auto Stop + Email)

## 📌 Objective
To configure a CloudWatch Alarm that triggers when EC2 CPU utilization exceeds 70%, automatically stops the instance, and sends an email notification.

This task demonstrates automated monitoring and infrastructure control in AWS.

---

## 🛠️ Services Used
- Amazon EC2
- Amazon CloudWatch
- Amazon SNS
- IAM Role (for EC2 actions)

---

## 🧠 Architecture Flow

1. CloudWatch monitors EC2 CPU utilization.
2. If CPU > 70%:
   - CloudWatch alarm triggers.
   - EC2 stop action is executed.
   - SNS sends email notification.

This ensures automated monitoring and cost control.

---

## 🌍 Implementation Steps

### Step 1: Create SNS Topic

1. Open AWS Console → SNS.
2. Click **Create Topic**.
3. Choose **Standard Topic**.
4. Enter topic name (e.g., CPU-Alert-Topic).
5. Create topic.
6. Create email subscription.
7. Confirm subscription from email.

---

### Step 2: Create CloudWatch Alarm

1. Open CloudWatch → Alarms.
2. Click **Create Alarm**.
3. Select metric:
   - EC2 → Per-Instance Metrics → CPUUtilization.
4. Choose specific EC2 instance.
5. Set condition:
   - Threshold type: Static
   - CPU ≥ 70%
   - Evaluation period: 1 minute (or as required)

---

### Step 3: Configure Alarm Actions

Under Alarm Actions:

1. Add notification:
   - Select SNS topic (CPU-Alert-Topic).

2. Add EC2 action:
   - Select **Stop this instance**.

3. Create alarm.

---

### Step 4: Test Alarm

1. Generate CPU load on EC2:

```bash
sudo apt install stress -y
stress --cpu 2 --timeout 300
```

2. Wait for CPU utilization to exceed 70%.
3. Verify:
   - Alarm state changes to ALARM.
   - EC2 instance stops automatically.
   - Email notification received.

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot showing:
   - CloudWatch alarm configuration (CPU ≥ 70%).

2. Screenshot showing:
   - EC2 instance state changed to Stopped + Email received.

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Concepts Learned

### 📊 CloudWatch Monitoring
- Tracks EC2 performance metrics.
- Enables automated alerting.

### ⚙️ Automated EC2 Action
- CloudWatch can perform stop, terminate, reboot, or recover actions.

### 📨 SNS Notification
- Sends email alert when threshold is breached.

---

## 📊 Why This is Important

- Prevents resource overuse.
- Helps reduce unexpected costs.
- Enables automated infrastructure management.
- Critical for production monitoring systems.

---

## 🎯 Conclusion

In this task, a CloudWatch alarm was successfully configured to monitor EC2 CPU utilization.  
When CPU usage exceeded 70%, the EC2 instance stopped automatically and an email alert was sent via SNS.

This demonstrates automated monitoring and infrastructure control in AWS.