# AWS Roadmap

This roadmap goes from basic cloud confidence to real DevOps-style AWS work.

## Stage 1 - Cloud Basics

Learn:

- What cloud computing is: on-demand compute, storage, networking, databases.
- Shared responsibility model: AWS secures the cloud; you secure what you put
  in the cloud.
- Regions and Availability Zones.
- Basic pricing: pay for usage, data transfer, storage, running time.
- Free Tier limits and why "free" still needs budgets.

Practice:

```bash
aws --version
aws sts get-caller-identity
aws configure list
```

## Stage 2 - Core AWS Services

Learn:

- IAM: users, groups, roles, policies.
- S3: object storage.
- EC2: virtual machines.
- VPC: networking boundary for your cloud resources.
- Security Groups: instance-level firewall rules.
- RDS: managed relational databases.
- CloudWatch: logs, metrics, alarms.

Practice:

```bash
aws s3 ls
aws ec2 describe-regions --output table
aws iam get-user
```

## Stage 3 - Security First

Learn:

- Never use the root user for daily work.
- Use MFA.
- Prefer IAM Identity Center or roles over long-lived access keys.
- Apply least privilege.
- Store secrets in Secrets Manager or SSM Parameter Store, not Git.
- Enable CloudTrail and budget alerts early.

Practice:

```bash
aws cloudtrail describe-trails
aws budgets describe-budgets --account-id YOUR_ACCOUNT_ID
aws iam list-policies --scope Local
```

## Stage 4 - Infrastructure As Code

Learn:

- Terraform provider configuration.
- Remote state in S3 with DynamoDB locking.
- Variables, outputs, modules, environments.
- Plan review before apply.
- Importing existing resources carefully.

Practice:

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
```

## Stage 5 - Containers On AWS

Learn:

- Docker images and containers.
- ECR for private image registry.
- ECS/Fargate for running containers without managing servers.
- Load balancing with ALB.
- Logs in CloudWatch.

Practice:

```bash
docker build -t demo-app .
aws ecr get-login-password --region ap-south-1
aws ecs list-clusters
```

## Stage 6 - Advanced DevOps

Learn:

- Multi-account setup.
- CI/CD with GitHub Actions, CodePipeline, or Jenkins.
- Blue/green deployments.
- Autoscaling.
- Observability.
- Disaster recovery.
- Cost optimization.

Practice:

```bash
aws cloudwatch describe-alarms
aws autoscaling describe-auto-scaling-groups
aws ce get-cost-and-usage --time-period Start=2026-06-01,End=2026-06-12 --granularity MONTHLY --metrics UnblendedCost
```
