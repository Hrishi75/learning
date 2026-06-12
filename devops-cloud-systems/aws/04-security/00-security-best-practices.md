# AWS Security Best Practices

Security is not a separate final step. Treat it as part of every command,
Terraform file, Dockerfile, and deployment.

## Account Security

Do:

- Enable MFA on root.
- Do not use root for daily work.
- Create budget alerts.
- Use IAM Identity Center for human access.
- Keep separate accounts or environments for dev/stage/prod when possible.

Avoid:

- Sharing the root login.
- Creating access keys for root.
- Keeping old IAM users forever.
- Using one admin user for every task.

## IAM

Best practices:

- Prefer roles and temporary credentials.
- Use least privilege.
- Use groups/permission sets for humans.
- Rotate or remove unused access keys.
- Add conditions to policies where possible.
- Do not use wildcard permissions unless there is a clear reason.

Inspect:

```bash
aws iam get-account-summary
aws iam list-access-keys --user-name USER_NAME
aws iam get-account-password-policy
aws iam list-attached-user-policies --user-name USER_NAME
```

Example least-privilege policy idea:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::my-learning-bucket"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-learning-bucket/*"
    }
  ]
}
```

## Network Security

Best practices:

- Expose only required ports.
- Restrict SSH/RDP to your IP.
- Put databases in private subnets.
- Use load balancers instead of public app servers when possible.
- Use HTTPS for public applications.

Bad security group habit:

```text
0.0.0.0/0 on port 22
0.0.0.0/0 on database ports
```

Better:

```text
YOUR_PUBLIC_IP/32 on port 22
app-security-group -> database-security-group on port 5432
```

Inspect:

```bash
aws ec2 describe-security-groups --query "SecurityGroups[].{Name:GroupName,Ingress:IpPermissions}"
```

## Secrets

Never store secrets in:

- Git.
- Docker images.
- Terraform variables committed to Git.
- Plain text notes.
- User data scripts.

Use:

- AWS Secrets Manager.
- SSM Parameter Store.
- Environment variables injected by the runtime.
- CI/CD secret stores.

Commands:

```bash
aws secretsmanager list-secrets
aws ssm describe-parameters
```

## Encryption

Best practices:

- Enable S3 default encryption.
- Encrypt EBS volumes.
- Encrypt RDS storage.
- Use KMS customer-managed keys when you need stricter control.
- Limit who can decrypt data.

Commands:

```bash
aws kms list-keys
aws s3api get-bucket-encryption --bucket BUCKET_NAME
```

## Logging And Audit

Enable:

- CloudTrail for API activity.
- CloudWatch Logs for app and system logs.
- VPC Flow Logs for network troubleshooting.
- GuardDuty for threat detection in serious environments.

Commands:

```bash
aws cloudtrail describe-trails
aws logs describe-log-groups
aws guardduty list-detectors
```

## Terraform Security

Do:

- Use remote state with encryption.
- Lock state with DynamoDB or supported backend locking.
- Mark sensitive outputs.
- Do not commit state files.
- Run `terraform plan` before apply.
- Scan IaC with tools like Checkov or tfsec.

Avoid:

- Hardcoding access keys in provider blocks.
- Putting passwords in `.tfvars` committed to Git.
- Wide-open security groups.
- Public S3 buckets unless intentionally required.

## Docker Security On AWS

Do:

- Use minimal base images.
- Avoid running containers as root where possible.
- Scan images.
- Keep secrets out of Dockerfiles.
- Use ECR private repositories.
- Use ECS task roles for AWS permissions.

Avoid:

- `COPY . .` without `.dockerignore`.
- Secrets in image layers.
- `latest` tags for production.
- Privileged containers unless absolutely needed.
