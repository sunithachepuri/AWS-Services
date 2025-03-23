# aws rds create-db-instance 
    --db-instance-identifier mydb-cli \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username admin \
    --master-user-password sunitha17 \
    --backup-retention-period 7 \
    --publicly-accessible \
    --region us-east-1

# To check the status of the RDS instance
aws rds describe-db-instances --query "DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus]"

# Use this endpoint to connect via MySQL Workbench.
aws rds describe-db-instances --query "DBInstances[*].mydb-cli.c6dwqukgy354.us-east 1.rds.amazonaws.com"

# RDS configuration using python
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
MasterUserPassword="sunitha17!",  # Use a strong password
BackupRetentionPeriod=7,  # Keep backups for 7 days
PubliclyAccessible=True,  # Set to False if private
 )

print("RDS Instance Creation Started!")
print(response)
