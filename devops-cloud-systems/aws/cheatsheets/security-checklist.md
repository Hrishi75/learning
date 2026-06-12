# AWS Security Checklist

Use this before, during, and after AWS labs.

## Account

- Root MFA is enabled.
- Root user is not used for daily work.
- Budget alert exists.
- Default region is known.
- Account ID is not posted publicly unless needed.

## IAM

- Human access uses IAM Identity Center or MFA-protected users.
- No root access keys exist.
- Unused access keys are deleted.
- Permissions follow least privilege.
- Admin permissions are limited to admin tasks.
- Service permissions use roles.

## Networking

- SSH is not open to `0.0.0.0/0`.
- RDP is not open to `0.0.0.0/0`.
- Database ports are not public.
- Private resources are in private subnets.
- Security groups allow only required ports.
- Public IPs are used intentionally.

## Storage

- S3 Block Public Access is enabled unless public access is intentional.
- Important buckets have versioning.
- Buckets are encrypted.
- Lifecycle policies exist for logs/backups.
- Sensitive files are not uploaded publicly.

## Secrets

- No secrets are committed to Git.
- No secrets are baked into Docker images.
- No secrets are hardcoded in Terraform.
- Secrets Manager or SSM Parameter Store is used where appropriate.
- CI/CD secrets are scoped tightly.

## Logging

- CloudTrail is enabled for real environments.
- CloudWatch log groups have retention periods.
- Application logs are searchable.
- Security findings are reviewed.
- Billing alarms are monitored.

## Terraform

- `.terraform/` is ignored.
- State files are ignored.
- Remote state is encrypted.
- State bucket has versioning.
- Plans are reviewed before apply.
- Every resource has tags.

## Docker

- `.dockerignore` exists.
- Images are scanned.
- Containers do not run as root unless needed.
- Image tags are meaningful.
- AWS permissions come from task roles, not keys in containers.

## Cleanup

- EC2 instances are stopped or terminated.
- EBS volumes and snapshots are reviewed.
- Load balancers are deleted.
- NAT Gateways are deleted.
- ECR repositories from labs are deleted.
- CloudWatch logs are cleaned or retention is set.
- Terraform labs are destroyed when done.
