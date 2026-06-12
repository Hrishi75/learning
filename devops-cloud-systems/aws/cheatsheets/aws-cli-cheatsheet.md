# AWS CLI Cheat Sheet

## Identity And Config

```bash
aws --version
aws configure list
aws configure list-profiles
aws sts get-caller-identity
aws sts get-caller-identity --profile PROFILE_NAME
export AWS_PROFILE=PROFILE_NAME
```

## Regions

```bash
aws ec2 describe-regions --output table
aws configure set region ap-south-1 --profile PROFILE_NAME
```

## S3

```bash
aws s3 ls
aws s3 mb s3://BUCKET_NAME --region ap-south-1
aws s3 cp file.txt s3://BUCKET_NAME/
aws s3 sync ./site s3://BUCKET_NAME/
aws s3 rm s3://BUCKET_NAME/file.txt
aws s3 rb s3://BUCKET_NAME
```

## EC2

```bash
aws ec2 describe-instances
aws ec2 describe-images --owners amazon
aws ec2 describe-security-groups
aws ec2 describe-key-pairs
aws ec2 stop-instances --instance-ids INSTANCE_ID
aws ec2 terminate-instances --instance-ids INSTANCE_ID
```

## VPC

```bash
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-route-tables
aws ec2 describe-internet-gateways
aws ec2 describe-nat-gateways
```

## IAM

```bash
aws iam get-account-summary
aws iam list-users
aws iam list-roles
aws iam list-policies --scope Local
aws iam list-access-keys --user-name USER_NAME
```

## CloudWatch

```bash
aws logs describe-log-groups
aws logs describe-log-streams --log-group-name LOG_GROUP
aws logs tail LOG_GROUP --follow
aws cloudwatch describe-alarms
```

## ECR

```bash
aws ecr create-repository --repository-name APP_NAME
aws ecr list-images --repository-name APP_NAME
aws ecr get-login-password --region ap-south-1
aws ecr delete-repository --repository-name APP_NAME --force
```

## ECS

```bash
aws ecs list-clusters
aws ecs list-services --cluster CLUSTER_NAME
aws ecs list-tasks --cluster CLUSTER_NAME
aws ecs describe-services --cluster CLUSTER_NAME --services SERVICE_NAME
aws ecs describe-tasks --cluster CLUSTER_NAME --tasks TASK_ID
```

## Query Examples

```bash
aws ec2 describe-regions --query "Regions[].RegionName" --output text
aws sts get-caller-identity --query Account --output text
aws s3api list-buckets --query "Buckets[].Name" --output table
```

## Cleanup Discovery

```bash
aws resourcegroupstaggingapi get-resources
aws resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=aws-learning
```
