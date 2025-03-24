# Amazon Elastic Container Registry (ECR) - Overview

## What is AWS ECR?

Amazon Elastic Container Registry (ECR) is a fully managed container image registry that allows you to store, manage, and deploy Docker

container images securely. It is designed for seamless integration with AWS services like Amazon ECS (Elastic Container Service), EKS

(Elastic Kubernetes Service), and AWS Lambda.

### Key Features of AWS ECR

✅ Fully Managed: No need to maintain your own container registry.

✅ Secure: Images are encrypted and can be controlled using AWS IAM permissions.

✅ Highly Available: Replicated across multiple AWS Availability Zones.

✅ Public & Private Repositories: Host images either privately or publicly.

✅ Integrated Image Scanning: Detect vulnerabilities in your container images.

✅ Seamless AWS Integration: Works with ECS, EKS, and CI/CD pipelines.

### Use Cases of AWS ECR

✅ Store and manage Docker images for AWS services (ECS, EKS, Lambda).

✅ Securely manage container images using AWS IAM policies.

✅ Automate CI/CD pipelines with AWS CodePipeline & Jenkins.

✅ Deploy containerized applications in a scalable manner.

### Create ECR by AWS console

Create a public/private ECR repository.

<img width="1439" alt="Screenshot 2025-03-24 at 9 16 43 AM" src="https://github.com/user-attachments/assets/5a4e0c3f-fbe4-43ab-a3dc-b5a38a0da357" />

### Create ECR by AWS CLI

Configure AWS CLI with you credentials

aws configure

aws ecr create-repository --repository-name my-hello-world-repository --region us-east-1

                




