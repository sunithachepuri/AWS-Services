# ECS 
Overview
Elastic Container Service (ECS) is a container orchestration service that automates the deployment, management, and scaling of Docker containers without the complexity of maintaining your own container infrastructure.

Key Features
Maintains the desired count of tasks
Integrates with AWS Fargate (serverless) and EC2 instances for container management
Key Components of AWS ECS
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
