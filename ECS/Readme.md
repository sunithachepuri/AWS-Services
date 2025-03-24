# ECS OVERVIEW & USUAGE GUIDE 

## Overview

Elastic Container Service (ECS) is a container orchestration service that automates the deployment, management, and scaling of Docker 

containers without the complexity of maintaining your own container infrastructure.

### Key Features

Maintains the desired count of tasks

Integrates with AWS Fargate (serverless) and EC2 instances for container management

### Key Components of AWS ECS

1. Clusters
   
Logical group of ECS resources (EC2 or Fargate) that manage groups of tasks or services.

EC2: Register and manage the EC2 instances yourself.

Fargate: Serverless, managed automatically.

External (ECS Anywhere): For on-premise servers, register and manage remotely.

2. Task Definitions
   
Blueprint that defines how a container should run, including:

CPU and memory allocation

Environment variables

IAM roles

3. Tasks
   
A running instance of a task definition.

4. Services
   
Ensures the desired number of tasks are running, supports auto-scaling, and integrates with Elastic Load Balancer (ELB).

5. Container Agent
   
Runs on EC2 instances and manages communication with ECS.

6. Load Balancing
    
Uses ALB/NLB for distributing traffic to ECS tasks:

Application Load Balancer (ALB): Handles HTTP/HTTPS traffic with advanced routing.

Network Load Balancer (NLB): Manages TCP/UDP traffic for high performance and low latency.

Classic Load Balancer (CLB): Legacy load balancer.

### create a ECS using AWS console

Sign in to AWS Console → Open AWS ECS Console and Create ECS Cluster


<img width="1440" alt="Screenshot 2025-03-24 at 4 24 49 PM" src="https://github.com/user-attachments/assets/7e756a00-6b52-4093-9c16-7a760dad6296" />


Create Task Definition

<img width="1381" alt="Screenshot 2025-03-24 at 4 27 04 PM" src="https://github.com/user-attachments/assets/b9601af7-ebbb-45a5-b9ae-362cbd2b0271" />

Create Service under  ECS Cluster then Deploy

### create ECS using AWS CLI

configure AWS CLI with your credentials

aws configure

```sh
aws ecs create-cluster --cluster-name my-ecs-cluster
```

Register ECS Task Definition

```sh
aws ecs register-task-definition --family my-task-def \
    --network-mode awsvpc \
    --requires-compatibilities FARGATE \
    --cpu "256" --memory "512" \
    --container-definitions '[{
        "name": "my-container",
        "image": "221082201013.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo:latest",
        "essential": true,
        "portMappings": [{"containerPort": 80, "hostPort": 80}]
    }]'
```

Run Task in ECS Cluster

```sh
aws ecs create-service --cluster my-ecs-cluster --service-name my-ecs-service \
    --task-definition my-task-def --desired-count 1 --launch-type FARGATE
```
<img width="1252" alt="Screenshot 2025-03-24 at 5 00 03 PM" src="https://github.com/user-attachments/assets/24c2b367-98e9-4af4-a65f-5761b5d3fcd5" />

