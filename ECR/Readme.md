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

### Create ECR by python Boto3

build a sample Docker image, and push it to ECR

Installing all the dependencies 

```sh
pip install boto3
pip install awscli
```
Install docker

```sh
brew install --cask docker
```
Set up AWS credentials

```sh
aws configure
```
Create a python script and run the script 

```sh
python create_ecr.py
```

```sh
import boto3

# Create ECR client
ecr_client = boto3.client("ecr", region_name="us-east-1")  # Change region if needed

repository_name = "my-sample-repo"

try:
    response = ecr_client.create_repository(repositoryName=repository_name)
    repository_uri = response["repository"]["repositoryUri"]
    print(f"Repository Created: {repository_uri}")
except ecr_client.exceptions.RepositoryAlreadyExistsException:
    print(f"Repository '{repository_name}' already exists.")
```

Now authenticate Docker to ECR

```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 221082201013.dkr.ecr.us-east-1.amazonaws.com
```

<img width="1440" alt="Screenshot 2025-03-24 at 3 58 03 PM" src="https://github.com/user-attachments/assets/baf73c81-d497-4b2e-861f-26dfcdf6951e" />

create a my-smaple-app directory and a dockerfile inside the directory for the project and navigate into it.

```sh
# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application file to the container
COPY app.py .

# Define the command to run the application
CMD ["python", "app.py"]
```

This docker file uses a lightweight Python image (python:3.9-slim) as the base.

Sets /app as the working directory.

Copies app.py into the container.

Runs app.py when the container starts.

Create the app.py file in the same directory and add the following simple Python script:

```sh
print("Hello from Docker!")
```

<img width="836" alt="Screenshot 2025-03-24 at 3 56 53 PM" src="https://github.com/user-attachments/assets/a83302a0-a20d-4ca9-ab13-d8d101b17a67" />

build the docker image 

```sh
docker build -t my-sample-image .
```

Verify docker images 

```sh
docker images
```

<img width="837" alt="Screenshot 2025-03-24 at 3 35 21 PM" src="https://github.com/user-attachments/assets/effd29fb-21ec-4f9d-8ae0-b2584842134c" />

Tag the docker image

```sh
docker tag my-sample-image:latest 221082201013.dkr.ecr.us-east-1.amazonaws.com/my-sample-repo:latest
```

Push the docker image to ECR 

```sh
docker push 221082201013.dkr.ecr.us-east-1.amazonaws.com/my-sample-repo:latest
```
To pull and run the image

```sh
docker pull 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-sample-repo:latest
docker run --rm 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-sample-repo:latest
```

Now, the Docker image is stored in AWS ECR and can be used in your CI/CD pipelines or Kubernetes clusters.


<img width="830" alt="Screenshot 2025-03-24 at 3 44 19 PM" src="https://github.com/user-attachments/assets/8bcad23a-e086-4e6c-8f52-5c75a645df7f" />

<img width="1082" alt="Screenshot 2025-03-24 at 4 06 49 PM" src="https://github.com/user-attachments/assets/dbaa8400-7c58-4460-9184-faf3c0b7ca12" />








               




