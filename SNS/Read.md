# SNS OVERVIEW & USUAGE GUIDE

## What is AWS SNS?

AWS Simple Notification Service (SNS) is a fully managed messaging service that allows you to send notifications or messages to multiple 

subscribers using various communication channels.

### Key Features of SNS

 Publish-Subscribe Model → One-to-many messaging system
 
 Multiple Protocols Supported → Email, SMS, HTTP, AWS Lambda, SQS
 
 Event-Driven → Works well with AWS services like S3, EC2, Lambda
 
 Scalable & Serverless → Automatically handles high traffic
 
 FIFO Topics → Ensures message ordering and deduplication (for SQS)

### How AWS SNS Works

 Publisher sends a message to an SNS Topic.

 SNS Topic distributes the message to all subscribers.

 Subscribers (Email, SMS, HTTP, SQS, Lambda) receive the message.

📌 Example: You create an SNS topic and subscribe your email to it. When a message is published, AWS SNS sends an email notification to your inbox.

### Types of SNS Topics

#### Standard Topic (default)

High throughput, best-effort delivery

Messages may be delivered out of order

Supports all subscribers (Email, SMS, HTTP, Lambda, SQS)

Use case: General notifications (e.g., system alerts, user notifications)

### FIFO (First-In-First-Out) Topic

Message order is guaranteed

Exactly-once delivery

Only supports AWS SQS as a subscriber

Use case: Financial transactions, inventory management

Create SNS by AWS Console

<img width="1072" alt="Screenshot 2025-03-23 at 7 14 43 PM" src="https://github.com/user-attachments/assets/b434c14e-990f-410d-a5a4-9795c9439372" />

