
# What is AWS SNS?
AWS Simple Notification Service (SNS) is a fully managed messaging service that allows you to send notifications or messages to multiple subscribers using various communication channels.

## Key Features of SNS
✅ Publish-Subscribe Model → One-to-many messaging system
✅ Multiple Protocols Supported → Email, SMS, HTTP, AWS Lambda, SQS
✅ Event-Driven → Works well with AWS services like S3, EC2, Lambda
✅ Scalable & Serverless → Automatically handles high traffic
✅ FIFO Topics → Ensures message ordering and deduplication (for SQS)

## How AWS SNS Works
1️⃣ Publisher sends a message to an SNS Topic.
2️⃣ SNS Topic distributes the message to all subscribers.
3️⃣ Subscribers (Email, SMS, HTTP, SQS, Lambda) receive the message.

📌 Example: You create an SNS topic and subscribe your email to it. When a message is published, AWS SNS sends an email notification to your inbox.

4️⃣ Types of SNS Topics
1️⃣ Standard Topic (default)

High throughput, best-effort delivery
Messages may be delivered out of order
Supports all subscribers (Email, SMS, HTTP, Lambda, SQS)
Use case: General notifications (e.g., system alerts, user notifications)
2️⃣ FIFO (First-In-First-Out) Topic

Message order is guaranteed
Exactly-once delivery
Only supports AWS SQS as a subscriber
Use case: Financial transactions, inventory management
