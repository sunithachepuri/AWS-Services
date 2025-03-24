# SNS by AWS CLI configuration

curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
aws configure 

# create SNS via CLI

aws sns create-topic --name my-sns-cli

# Send an SMS message 

aws sns subscribe \
  --topic-arn "arn:aws:sns:us-east-1:221082201013:my-sns-cli" \
  --protocol sms \
  --notification-endpoint "+8722795542"

# verify SMS delivery

aws sns get-sms-attributes

#SNS by using python Boto3

pip install boto3

aws configure

# run the script to create sns topic python create_sns.py

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

# run the script to subscribe to the topic python subscribe_sns.py


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

# run the script to publish the message python publish_message.py


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



