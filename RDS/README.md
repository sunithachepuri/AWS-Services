# RDS OVERVIEW & USAGE GUIDE 
  
  ## What is Amazon RDS?
  Amazon RDS is a fully managed relational database service that simplifies database operations, maintenance, and scaling.

  ### Advantages of RDS
  
  Managed Database: AWS handles backups, scaling, security, and maintenance.
  
  High Availability: Supports Multi-AZ deployments.
  
  Automatic Backups: Enables daily backups and snapshots.

  Scalability: Easily scale storage and compute resources.

  Security: Supports IAM roles, encryption, and VPC isolation.

  ### Common Use Cases
  
  Web Applications: Use RDS as the backend database for high-performance, scalable applications.

  Data Warehousing: Store structured data for reporting and analytics with tools like Tableau, Power BI, and AWS Redshift.

  ETL Pipelines: Serve as an intermediate storage layer for extracting, transforming, and loading (ETL) data.

  Multi-Tenant Applications: Support multiple users with isolated databases for SaaS platforms.

  Machine Learning Workloads: Store processed data before feeding it into AWS SageMaker or other ML models.

  Disaster Recovery: Enable automated failover with Multi-AZ deployments and snapshots.

  Hybrid Cloud Integration: Extend on-premises databases into the cloud for scalability and reliability.

  ### RDS Configuration using AWS CONSOLE
  
  1. Create an RDS Instance

     Create a standard database by choosing MySQL as a database engine and set up a username: admin, password: sunitha17

     Configure VPC connectivity with port number 3306 in inbound rule then AWS starts creating RDS instance

     <img width="1143" alt="1" src="https://github.com/user-attachments/assets/3faf596c-9472-4e76-8452-7c648f2ea898" />

  2. Connect Using MySQL Workbench
     
     Open MySQL Workbench.
     
     Click + to add a new connection.

     Set up connection details:
     
     Connection Name: AWS RDS MySQL
     
     Hostname: mydb-instance.123456789012.us-east-1.rds.amazonaws.com
     
     Port: 3306
     
     Username: admin
     
     Password: Sunitha17
     
     Click Test Connection → If successful, click OK.
     
     <img width="1406" alt="2" src="https://github.com/user-attachments/assets/a3270d61-da70-4f6c-a4d4-c6ab02bbf1ac" />

  ### RDS Configuration Using AWS CLI

   1. Ensure AWS CLI is installed and configured:
  
   Provide:
   AWS Access Key,
   AWS Secret Key,
   Default region (e.g., us-east-1)

   <img width="574" alt="Screenshot 2025-03-20 at 11 02 04 PM" src="https://github.com/user-attachments/assets/d87312b2-c239-4917-8b4c- 5b8860f03591" />



  






