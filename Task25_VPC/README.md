# Task 25 — Highly Available Web Application (High Availability Architecture)

## Objective

Create a fault-tolerant web application where the website continues to run even if one server stops.
The setup uses private networking, load balancing, auto scaling and monitoring.


## Step 1 — Create VPC

* Created VPC named **my-vpc**
* CIDR block: `10.0.0.0/16`


## Step 2 — Create Subnets

Created four subnets:

**Public**

* public-subnet-1 (10.0.1.0/24)
* public-subnet-2 (10.0.2.0/24)

**Private**

* private-subnet-1 (10.0.3.0/24)
* private-subnet-2 (10.0.4.0/24)

Enabled **Auto-assign Public IPv4** only for public subnets.


## Step 3 — Internet Gateway

* Created Internet Gateway: **my-igw**
* Attached it to VPC (my-vpc)


## Step 4 — Public Route Table

* Created **public-route-table**
* Added route: `0.0.0.0/0 → my-igw`
* Associated with:

  * public-subnet-1
  * public-subnet-2


## Step 5 — NAT Gateway

* Created NAT Gateway: **MY-NAT-GW**
* Placed inside public-subnet-1
* Allocated Elastic IP



## Step 6 — Private Route Table

* Created **private-route-table**
* Added route: `0.0.0.0/0 → MY-NAT-GW`
* Associated with:

   private-subnet-1
   private-subnet-2


## Step 7 — Launch Private Servers

Launched two Ubuntu instances:

 Instance     Subnet           
 webserver-1  private-subnet-1
 webserver-2  private-subnet-2 

* No public IP assigned
* SSH allowed only from Bastion security group
* HTTP port 80 allowed

---

## Step 8 — Bastion Host

Created one public instance:

**bastion**

* Placed in public-subnet-1
* Public IP enabled
* Used to SSH into private servers

Connected:
Laptop → Bastion → Private Servers

---

## Step 9 — Install Web Server

Connected to each private server via bastion and installed Apache:

```
sudo apt update -y
sudo apt install apache2 -y
sudo systemctl start apache2
sudo systemctl enable apache2
```

Created web pages:

**webserver-1**

```
<h1>Server 1 Working</h1>
<h2>High Availability Test</h2>
```

**webserver-2**

```
<h1>Server 2 Working</h1>
<h2>High Availability Test</h2>
```

Tested using:

```
curl localhost
```

---

## Step 10 — Target Group

Created target group:
**web-targets**

* Protocol: HTTP
* Port: 80
* Registered both instances (webserver-1 and webserver-2)

---

## Step 11 — Load Balancer

Created Application Load Balancer:

* Internet-facing
* Attached to:

  * public-subnet-1
  * public-subnet-2
* Connected to target group (web-targets)

Verified:
Refreshing DNS URL switched between both servers.

---

## Step 12 — AMI & Launch Template

Created image from webserver-1:
**webserver-image**

Created launch template:
**web-template**

* Used the created AMI
* Disabled public IP
* Same security group

User data:

```
#!/bin/bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

---

## Step 13 — Auto Scaling Group

Created Auto Scaling Group:
**web-ASG**

Settings:

* VPC: my-vpc
* Subnets: private-subnet-1 & private-subnet-2
* Desired: 2
* Minimum: 2
* Maximum: 4
* Attached to target group (web-targets)

---

## Step 14 — Cloud Monitoring Alarm

Created CPU alarm:

* Metric: CPUUtilization
* Condition: CPU > 70%

Scaling policy:

* Add 1 instance when alarm triggers

---

## Step 15 — Scaling Test

Installed stress tool on an ASG instance:

```
sudo apt install stress -y
stress --cpu 2 --timeout 300
```

Observed:

* Alarm state changed
* New instance launched automatically
* Became healthy in target group
* Website continued working

---

## High Availability Test

Stopped one server manually.
Website still opened successfully through load balancer.

---

## Result

A highly available architecture was implemented where:

* Load balancer distributes traffic
* Auto Scaling launches new servers
* Monitoring triggers scaling
* Website remains available even after server failure
