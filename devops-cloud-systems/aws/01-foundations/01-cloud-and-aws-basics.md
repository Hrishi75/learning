# Cloud And AWS Basics

## What Cloud Computing Means

Cloud computing means renting computing resources from a provider instead of
buying and maintaining physical servers yourself.

Common cloud resources:

- Compute: virtual machines, containers, serverless functions.
- Storage: object storage, disks, file systems.
- Networking: private networks, public IPs, DNS, firewalls.
- Databases: managed SQL, NoSQL, cache, data warehouses.
- Security: identity, permissions, encryption, audit logs.

## AWS Global Infrastructure

AWS is organized as:

- Region: a geographic area, such as `ap-south-1` or `us-east-1`.
- Availability Zone: an isolated data center group inside a region.
- Edge location: used by services like CloudFront for low-latency delivery.

Best practice:

- Pick one main region for learning. For India, `ap-south-1` is common.
- Deploy production workloads across at least two Availability Zones.
- Avoid creating test resources across many regions because it becomes hard to
  track cost and cleanup.

## Shared Responsibility Model

AWS handles:

- Physical data centers.
- Hardware.
- Global network.
- Managed service infrastructure.

You handle:

- IAM permissions.
- Data protection.
- Security group rules.
- OS patching for EC2 instances.
- Application security.
- Secrets management.
- Resource cleanup and cost control.

## Basic AWS Account Safety

Do this before labs:

1. Add MFA to the root user.
2. Create an admin user or permission set for daily work.
3. Stop using the root user except for account-level tasks.
4. Create a budget alert.
5. Pick a default region.
6. Keep a cleanup checklist for every project.

## Common Service Categories

| Category | Services |
|----------|----------|
| Compute | EC2, Lambda, ECS, EKS, Elastic Beanstalk |
| Storage | S3, EBS, EFS, Glacier |
| Networking | VPC, Subnets, Route Tables, NAT Gateway, ALB, Route 53 |
| Database | RDS, DynamoDB, ElastiCache, Aurora |
| Security | IAM, KMS, Secrets Manager, CloudTrail, GuardDuty |
| Monitoring | CloudWatch, X-Ray, CloudTrail |
| DevOps | CodeBuild, CodePipeline, CodeDeploy, ECR |

## Cost Awareness

Things that often create unexpected bills:

- NAT Gateways left running.
- EC2 instances not stopped or terminated.
- Load balancers left after a lab.
- Large EBS volumes and snapshots.
- Data transfer out of AWS.
- RDS databases running 24/7.
- CloudWatch logs retained forever.

Habit:

```bash
aws resourcegroupstaggingapi get-resources --region ap-south-1
```

Use tags on every resource:

```text
Project=aws-learning
Owner=your-name
Environment=dev
ManagedBy=terraform
```
