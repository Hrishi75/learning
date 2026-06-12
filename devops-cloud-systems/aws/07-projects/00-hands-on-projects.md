# Hands-On AWS Projects

Build these in order. Each project teaches one practical skill and one cleanup
habit.

## Project 1 - Read-Only CLI Confidence

Goal:

- Confirm your CLI profile, region, and identity.

Commands:

```bash
aws sts get-caller-identity
aws configure list
aws ec2 describe-regions --output table
aws iam get-account-summary
```

Done when:

- You know which account and region your CLI is using.

## Project 2 - Private S3 Bucket

Goal:

- Create a private encrypted S3 bucket, upload a file, then remove everything.

Commands:

```bash
aws s3 mb s3://YOUR_UNIQUE_BUCKET_NAME --region ap-south-1
aws s3api put-public-access-block --bucket YOUR_UNIQUE_BUCKET_NAME --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-versioning --bucket YOUR_UNIQUE_BUCKET_NAME --versioning-configuration Status=Enabled
echo "hello aws" > hello.txt
aws s3 cp hello.txt s3://YOUR_UNIQUE_BUCKET_NAME/
aws s3 ls s3://YOUR_UNIQUE_BUCKET_NAME/
aws s3 rm s3://YOUR_UNIQUE_BUCKET_NAME/hello.txt
aws s3 rb s3://YOUR_UNIQUE_BUCKET_NAME
```

Security lesson:

- S3 should be private by default.

## Project 3 - EC2 Web Server

Goal:

- Launch a tiny EC2 instance, allow HTTP, restrict SSH, and clean up.

Learn:

- AMI, instance type, key pair, security group, user data.

Best practices:

- Use `t3.micro` or Free Tier-eligible equivalent where available.
- Open SSH only to your IP.
- Terminate the instance after the lab.

Cleanup:

```bash
aws ec2 terminate-instances --instance-ids INSTANCE_ID
```

## Project 4 - Basic VPC

Goal:

- Understand public/private subnet design.

Build:

- One VPC.
- Two public subnets.
- Two private subnets.
- Internet Gateway.
- Route table.

Best practices:

- Use two Availability Zones.
- Avoid NAT Gateway in first labs unless required.
- Tag every resource.

## Project 5 - Terraform S3 Bucket

Goal:

- Create the private S3 bucket from Project 2 using Terraform.

Workflow:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
terraform destroy
```

Done when:

- You can explain the difference between Terraform configuration and state.

## Project 6 - Terraform Remote State

Goal:

- Store Terraform state in S3 and use locking.

Build:

- S3 bucket for state.
- DynamoDB table for locks.
- Backend config.

Best practices:

- Enable versioning on state bucket.
- Enable encryption.
- Restrict state bucket access.

## Project 7 - Docker Image To ECR

Goal:

- Build a local Docker image and push it to ECR.

Steps:

```bash
docker build -t demo-app:dev .
aws ecr create-repository --repository-name demo-app --image-scanning-configuration scanOnPush=true
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com
docker tag demo-app:dev ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com/demo-app:dev
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com/demo-app:dev
```

Cleanup:

```bash
aws ecr delete-repository --repository-name demo-app --force
```

## Project 8 - ECS/Fargate Web App

Goal:

- Run your ECR image on ECS/Fargate.

Build:

- ECR repository.
- ECS cluster.
- Task definition.
- ECS service.
- CloudWatch logs.
- Optional ALB.

Best practices:

- Use task execution role and task role separately.
- Do not put AWS keys inside containers.
- Add health checks.
- Destroy the lab after testing.

## Project 9 - CI/CD To AWS

Goal:

- Push code to GitHub and deploy a container image automatically.

Build:

- GitHub Actions workflow.
- OIDC role in AWS.
- ECR push.
- ECS service update.

Best practices:

- Use OIDC instead of long-lived GitHub secrets when possible.
- Use immutable image tags such as commit SHA.
- Require review before production deploy.

## Project 10 - Production-Style Mini Platform

Goal:

- Combine VPC, ECS, ALB, CloudWatch, Terraform modules, and CI/CD.

Build:

- `dev` and `prod` environments.
- Shared modules.
- Remote state.
- Private subnets.
- ALB public entrypoint.
- ECS service autoscaling.
- CloudWatch alarms.

Done when:

- You can recreate the environment from Git and explain every major resource.
