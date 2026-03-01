# Task 12 - Website Down Alert using Lambda (Canary) + SNS

## 📌 Objective
To monitor website uptime using AWS Synthetics Canary and trigger an email alert using SNS when the website becomes unavailable.

This task demonstrates automated monitoring and alerting using AWS serverless services.

---

## 🛠️ Services Used
- Amazon CloudWatch Synthetics (Canary)
- AWS Lambda (managed by Canary)
- Amazon SNS
- IAM Role
- CloudWatch Alarms

---

## 🧠 Architecture Flow

1. Canary periodically checks website URL.
2. If website is down or returns error:
3. CloudWatch alarm triggers.
4. SNS sends email notification.

This is a fully automated monitoring system.

---

## 🌍 Implementation Steps

### Step 1: Create SNS Topic

1. Open AWS Console → SNS.
2. Click **Create Topic**.
3. Choose **Standard Topic**.
4. Enter topic name (e.g., Website-Down-Alert).
5. Create topic.
6. Create subscription:
   - Protocol: Email
   - Endpoint: Your email address.
7. Confirm email subscription.

---

### Step 2: Create Canary

1. Open AWS Console → CloudWatch.
2. Go to **Synthetics Canaries**.
3. Click **Create Canary**.
4. Select blueprint:
   - Heartbeat monitoring.
5. Enter:
   - Website URL (e.g., http://your-website.com).
6. Set schedule:
   - Run every 1 minute.
7. Create new IAM role automatically.
8. Create Canary.

Canary automatically creates Lambda function in background.

---

### Step 3: Create CloudWatch Alarm

1. Go to CloudWatch → Alarms.
2. Click **Create Alarm**.
3. Select Canary metric:
   - Failed or SuccessPercent.
4. Condition:
   - Trigger when failure > 0.
5. Select SNS topic for notification.
6. Create alarm.

---

### Step 4: Test the Setup

1. Stop your web server (or change security group to block traffic).
2. Wait for Canary to run.
3. CloudWatch detects failure.
4. SNS sends email alert.

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot showing:
   - Canary configuration with URL.

2. Screenshot showing:
   - CloudWatch alarm linked to SNS.

3. Screenshot showing:
   - Email alert received when website is down.

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Concepts Learned

### 🌐 Canary Monitoring
- Simulates user behavior.
- Continuously checks website availability.

### 🚨 CloudWatch Alarm
- Monitors metrics.
- Triggers actions when threshold breached.

### 📨 SNS Alerting
- Sends automated notifications.

---

## 📊 Why This is Important

- Detects downtime automatically.
- Enables proactive monitoring.
- Reduces manual supervision.
- Essential for production environments.

---

## 🎯 Conclusion

In this task, a website monitoring system was successfully implemented using CloudWatch Synthetics Canary and SNS alerts.

The system automatically detects website downtime and sends email notifications, demonstrating automated monitoring and alerting in AWS.