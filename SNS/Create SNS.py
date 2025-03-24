# AWS CLI configuration

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


