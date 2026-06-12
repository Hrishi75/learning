# Core AWS Services

This file is the quick map of AWS services you should learn first.

## IAM - Identity And Access Management

Purpose:

- Controls who can do what in AWS.

Core pieces:

- User: human or legacy identity.
- Group: collection of users.
- Role: assumed identity, best for services and temporary access.
- Policy: JSON permissions document.

Best practices:

- Use MFA.
- Use roles instead of long-lived keys.
- Grant least privilege.
- Avoid `AdministratorAccess` except for learning/admin roles.
- Review unused users, keys, and permissions.

Commands:

```bash
aws iam get-account-summary
aws iam list-users
aws iam list-roles
aws iam list-policies --scope Local
```

## S3 - Object Storage

Purpose:

- Store files as objects in buckets.

Common uses:

- Backups.
- Static websites.
- Logs.
- Terraform remote state.
- Data lakes.

Best practices:

- Block public access by default.
- Enable versioning for important buckets.
- Encrypt objects.
- Use lifecycle policies.
- Do not store secrets in public buckets.

Commands:

```bash
aws s3 mb s3://my-unique-learning-bucket
aws s3 cp file.txt s3://my-unique-learning-bucket/
aws s3 ls s3://my-unique-learning-bucket/
aws s3 rm s3://my-unique-learning-bucket/file.txt
aws s3 rb s3://my-unique-learning-bucket
```

## EC2 - Virtual Machines

Purpose:

- Run virtual servers.

Core pieces:

- AMI: server image.
- Instance type: CPU/memory size.
- Key pair: SSH access.
- Security group: firewall.
- EBS volume: disk.

Best practices:

- Use the smallest instance for labs.
- Allow SSH only from your IP.
- Use SSM Session Manager where possible.
- Patch the OS.
- Stop or terminate unused instances.

Commands:

```bash
aws ec2 describe-instances
aws ec2 describe-instance-types --instance-types t3.micro
aws ec2 describe-security-groups
```

## VPC - Networking

Purpose:

- Private network boundary for AWS resources.

Core pieces:

- VPC CIDR block.
- Public and private subnets.
- Route tables.
- Internet Gateway.
- NAT Gateway.
- Security Groups.
- Network ACLs.

Best practices:

- Use at least two Availability Zones for resilient apps.
- Put databases in private subnets.
- Keep public access only where needed.
- Avoid NAT Gateway in tiny labs unless you need it because it costs money.

Commands:

```bash
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-internet-gateways
```

## RDS - Managed Database

Purpose:

- Managed relational databases like PostgreSQL and MySQL.

Best practices:

- Keep databases private.
- Enable backups.
- Encrypt storage.
- Use strong passwords or Secrets Manager.
- Do not expose database ports to the internet.

Commands:

```bash
aws rds describe-db-instances
aws rds describe-db-subnet-groups
```

## CloudWatch - Monitoring

Purpose:

- Metrics, logs, dashboards, alarms.

Best practices:

- Set alarms for important metrics.
- Set log retention periods.
- Use structured application logs.
- Monitor billing and unexpected usage.

Commands:

```bash
aws logs describe-log-groups
aws cloudwatch describe-alarms
aws cloudwatch list-metrics --namespace AWS/EC2
```

## Route 53 - DNS

Purpose:

- Domain registration, hosted zones, DNS records, health checks.

Best practices:

- Use meaningful DNS names.
- Keep TTL low during migrations.
- Protect production hosted zones.
- Use health checks for critical endpoints.

Commands:

```bash
aws route53 list-hosted-zones
aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID
```

## Lambda - Serverless Functions

Purpose:

- Run code without managing servers.

Best practices:

- Keep functions small.
- Use IAM roles with least privilege.
- Put secrets in environment variables only if encrypted and controlled, or use
  Secrets Manager/SSM.
- Add timeouts and memory intentionally.
- Watch logs and retries.

Commands:

```bash
aws lambda list-functions
aws lambda get-function --function-name FUNCTION_NAME
```
