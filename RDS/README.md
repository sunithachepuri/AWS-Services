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

   <img width="574" alt="Screenshot 2025-03-20 at 11 02 04 PM" src="https://github.com/user-attachments/assets/6dcb70ad-1d1a-4f37-aee7-8e8b3c21a59c" />

   
  2. Create RDS Instance
      
   Run the following command to create a MySQL RDS instance:
   
   <img width="576" alt="Screenshot 2025-03-20 at 11 11 38 PM" src="https://github.com/user-attachments/assets/f56f5075-d2b6-45af-b789-ffa10ffa2496" />
   

   3. Run this to check the instance status:

    aws rds describe-db-instances --query "DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus]"
    

  4. Use this endpoint to connect via MySQL Workbench.

    aws rds describe-db-instances --query "DBInstances[*].mydb-cli.c6dwqukgy354.us-east 1.rds.amazonaws.com"
    

  5. Delete RDS Instance

    aws rds delete-db-instance \
    --db-instance-identifier mydb-cli \
    --skip-final-snapshot

### RDS Configuration Using Python (BOTO3)


    import boto3

    # Initialize the RDS client
    rds_client = boto3.client("rds", region_name="us-east-1")

    # Create RDS Instance
    response = rds_client.create_db_instance(
    DBInstanceIdentifier="my-rds-instance",
    AllocatedStorage=20,  # Storage in GB
    DBInstanceClass="db.t3.micro",  # Free-tier eligible
    Engine="mysql",  # Change to "postgres", "mariadb", etc.
    MasterUsername="admin",
    MasterUserPassword="YourStrongPassword123!",  # Use a strong password
    BackupRetentionPeriod=7,  # Keep backups for 7 days
    PubliclyAccessible=True,  # Set to False if private
     )

    print("RDS Instance Creation Started!")
    print(response)




     



   
   






  






