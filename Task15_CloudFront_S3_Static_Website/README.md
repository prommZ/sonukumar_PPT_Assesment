# Task 15 - CloudFront Distribution for S3 Static Website

## 📌 Objective
To configure Amazon CloudFront as a Content Delivery Network (CDN) for an S3 static website and understand global content distribution.

This task demonstrates how CDN improves performance, reduces latency, and enhances availability.

---

## 🛠️ Services Used
- Amazon S3
- Amazon CloudFront
- IAM (for permissions)

---

## 🖥️ Implementation Steps

### Step 1: Create S3 Static Website
1. Created an S3 bucket.
2. Uploaded index.html file.
3. Enabled "Static Website Hosting".
4. Configured bucket policy to allow public read access.
5. Verified website using S3 website endpoint.

---

### Step 2: Create CloudFront Distribution
1. Opened CloudFront console.
2. Clicked "Create Distribution".
3. Selected S3 bucket as origin.
4. Set default settings (Viewer Protocol Policy: Redirect HTTP to HTTPS).
5. Created distribution.

CloudFront generated a Domain Name (e.g., dxxxxx.cloudfront.net).

---

### Step 3: Test Website via CloudFront
1. Opened CloudFront domain URL in browser.
2. Verified that website loads successfully.
3. Confirmed faster and secure delivery (HTTPS enabled).

---

## 📷 Proof of Work (Screenshots Required)

1. Screenshot of S3 Static Website endpoint working.
2. Screenshot of CloudFront distribution details with domain name and status "Deployed".

(All screenshots inside the Screenshots folder.)

---

## 🔍 Key Learning

- S3 hosts static content.
- CloudFront caches content at Edge Locations globally.
- CDN reduces latency and improves user experience.
- HTTPS is automatically supported via CloudFront.

---

## 🎯 Conclusion

In this task, a CloudFront distribution was successfully configured for an S3 static website.  
The website was delivered globally through CloudFront edge locations, improving performance and security.

This demonstrates practical implementation of CDN and global content delivery in AWS.