TASK 13 – Start/Stop EC2 using Lambda + API Gateway + SNS

Lambda Name: Task13-Lambda
API Gateway: Task13-API
SNS Topic: Task13-topic
EC2 Instance: (my EC2 instance id)

Objective:
To automate EC2 start and stop using API Gateway and Lambda,
and send notification using SNS.

Services Used:
- AWS Lambda
- Amazon API Gateway
- Amazon SNS
- Amazon EC2
- IAM Role

What I did step by step:

1. First I created an IAM role for Lambda.
2. I attached permissions:
   - AmazonEC2FullAccess
   - AmazonSNSFullAccess

3. Then I created a Lambda function.
4. Function name:
   Task13-Lambda
5. Runtime:
   Python 3.x
6. I attached the IAM role to Lambda.

7. Inside Lambda, I wrote code to:
   - Start EC2 when action is "start"
   - Stop EC2 when action is "stop"

8. I deployed the Lambda function.

API Gateway (Trigger):

9. Then I added API Gateway as a trigger to Lambda.
10. I created a new HTTP API.
11. I integrated API Gateway with my Lambda function.
12. I created routes like:
    /start
    /stop
13. I deployed the API and copied the Invoke URL.

SNS (Destination):

14. I created an SNS topic:
    Task13-topic
15. I subscribed my email to the SNS topic.
16. I confirmed the subscription from email.

17. In Lambda → Destinations,
18. I added SNS as destination.
19. I selected SNS topic:
    Task13-topic
20. I configured:
    - On success → SNS
    - On failure → SNS

Testing:

21. I opened browser and called:
    InvokeURL/start
22. EC2 instance started successfully.
23. Lambda executed and SNS sent email notification.

24. I called:
    InvokeURL/stop
25. EC2 instance stopped successfully.
26. SNS email was received again.

Result:
EC2 start and stop is fully automated using API Gateway.
Lambda runs when API is called.
SNS sends email notification after Lambda execution.

Architecture Flow:
User → API Gateway → Lambda → EC2
                        ↓
                      SNS → Email

Proof:
- Screenshot of Lambda with API Gateway trigger
- Screenshot of SNS topic and email received
- Screenshot of EC2 state change