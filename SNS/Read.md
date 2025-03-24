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

## Create SNS by AWS Console

<img width="1072" alt="Screenshot 2025-03-23 at 7 14 43 PM" src="https://github.com/user-attachments/assets/b434c14e-990f-410d-a5a4-9795c9439372" />

Create Subscription to the SNS Topic 

<img width="1428" alt="Screenshot 2025-03-23 at 7 20 12 PM" src="https://github.com/user-attachments/assets/56b336ae-a3ad-440d-b489-b5dcde6b9cb2" />

Once created you will recieve a confirmation lik via email 

![IMG_1778](https://github.com/user-attachments/assets/10765ab4-648a-4015-b7a2-1bebc0091b9e)

After Confirming go to AWS SNS service and publish a message 

<img width="1416" alt="Screenshot 2025-03-23 at 7 18 01 PM" src="https://github.com/user-attachments/assets/01031a7a-7454-41cf-b700-cc15d4362643" />

Chcek you inbox!

![IMG_1777](https://github.com/user-attachments/assets/04bcd900-9892-4a00-9ba2-be1a11c04f67)


## Create SNS using AWS CLI

Install AWS CLI and congiure AWS CLI 

    curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"

    sudo installer -pkg AWSCLIV2.pkg -target /

    aws configure 

You'll be prompted to enter:

AWS Access Key ID:

AWS Secret Access Key:

Default region (e.g., us-east-1):

Output format (json, table, or text): 

Create SNS topic via CLI

    aws sns create-topic --name my-sns-cli
    
![image](https://github.com/user-attachments/assets/998c3a97-a350-42cf-96cf-9b964dbc36ab)


Send an SMS message to a single number or multiple numbers 

    aws sns subscribe \
      --topic-arn "arn:aws:sns:us-east-1:221082201013:my-sns-cli" \
      --protocol sms \
      --notification-endpoint "+8722795542"

Publish SMS to the subscribers       

    aws sns publish \
       --topic-arn "arn:aws:sns:us-east-1:221082201013:my-sns-cli" \
       --message "Hello, this is a broadcast SMS from AWS SNS!"


<img width="823" alt="Screenshot 2025-03-23 at 7 58 49 PM" src="https://github.com/user-attachments/assets/6e891742-bf74-4c67-96f7-f230bcbb41b2" />
       
Verify SMS delivery

    aws sns get-sms-attributes

 ## SNS by using Python Boto3 

 Install Boto3 lib using pip

       pip install boto3

Configure AWS CLI with the credentials

    aws configure

Write a python script to create an SNS topic and run script 
        
    python create_sns.py


    import boto3

    # Create an SNS client
    sns = boto3.client("sns", region_name="us-east-1")  # Change region if needed

    # Define a topic name
    topic_name = "sns_by_python"

    # Create the SNS topic
    response = sns.create_topic(Name=topic_name)

    # Get the topic ARN
    topic_arn = response["TopicArn"]
    print(f"SNS Topic Created: {topic_arn}")


Create another python script for subscription to the topic and run 

    python subscribe_sns.py


    import boto3

    # Create an SNS client
    sns = boto3.client("sns", region_name="us-east-1")

    # Replace with the ARN of your SNS topic
    topic_arn = "arn:aws:sns:us-east-1:221082201013:sns_by_python"  # Change this

    # Replace with the email or phone number you want to subscribe
    protocol = "email"  # Change to "sms" for phone numbers
    endpoint = "schepuri2@govst.edu"  

    # Subscribe to the topic
          response = sns.subscribe(
          TopicArn=topic_arn,
          Protocol=protocol,
          Endpoint=endpoint
    )

    # Print the subscription ARN
    print("Subscription ARN:", response["SubscriptionArn"])

Create a python script to publish a message and run the script 

    python publish_message.py


    import boto3

    # Create an SNS client
    sns = boto3.client("sns", region_name="us-east-1")

    # Replace with your SNS topic ARN
    topic_arn = "arn:aws:sns:us-east-1:221082201013:sns_by_python"

    # Message to send
    message = "Hello, this is a test message from AWS SNS!"

    # Publish the message
        response = sns.publish(
        TopicArn=topic_arn,
        Message=message
    )

    # Print message ID
    print("Message sent! Message ID:", response["MessageId"])

    <img width="1390" alt="Screenshot 2025-03-23 at 9 00 53 PM" src="https://github.com/user-attachments/assets/238127cc-5add-4d76-8745-3752b8ca2632" />


    
 

    

    


       


      





    

    







