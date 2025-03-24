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

```sh 
aws configure
```

Create a ECR repository named my-ecr-repo-cli

```sh
aws ecr create-repository --repository-name my-ecr-repo-cli --region us-east-1
```

<img width="1431" alt="Screenshot 2025-03-24 at 10 54 40 AM" src="https://github.com/user-attachments/assets/b62563be-1053-4f87-a353-86bb5e9b779d" />

Authenticate Docker to the registry to push and pull images from Amazon ECR

```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 221082201013.dkr.ecr.us-east-1.amazonaws.com
```

Pull the hello-world Docker image from Docker Hub

```sh
docker pull hello-world
```

Tag the hello-world Docker image to prepare it for pushing to your ECR repository

```sh
docker tag hello-world:latest 221082201013.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo-cli:latest
```

Push the tagged hello-world image to your ECR repository

```sh
docker push 221082201013.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo-cli:latest
```

<img width="595" alt="Screenshot 2025-03-24 at 11 05 52 AM" src="https://github.com/user-attachments/assets/389b05dc-c05f-41a0-b503-ee9ccdc5da8b" />

Run the Docker image locally

```sh
docker run hello-world
```

<img width="601" alt="Screenshot 2025-03-24 at 11 06 00 AM" src="https://github.com/user-attachments/assets/92c4e397-8ab0-449b-bbaf-3c18986c2177" />

               




