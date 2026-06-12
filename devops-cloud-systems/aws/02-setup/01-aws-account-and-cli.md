# AWS Account And CLI Setup

## Account Setup Checklist

Do this first:

1. Sign in as root only for initial account setup.
2. Enable MFA for root.
3. Create a budget.
4. Create an admin identity for daily work.
5. Choose a default region.
6. Log out from root and avoid daily root usage.

## Recommended Login Approach

Prefer IAM Identity Center for human users when possible.

Why:

- No long-lived access keys on your laptop.
- Easier MFA.
- Easier role-based access.
- Cleaner for real companies and teams.

## Configure AWS CLI With SSO

```bash
aws configure sso
```

You will be asked for:

- SSO start URL.
- SSO region.
- AWS account.
- Permission set/role.
- Default CLI region.
- Output format.

Login:

```bash
aws sso login --profile dev-admin
aws sts get-caller-identity --profile dev-admin
```

Use the profile:

```bash
export AWS_PROFILE=dev-admin
aws sts get-caller-identity
```

## Configure AWS CLI With Access Keys

Use this only for learning accounts or automation cases where SSO is not
available. Prefer short-lived credentials whenever possible.

```bash
aws configure --profile learning
```

You will enter:

- AWS Access Key ID
- AWS Secret Access Key
- Default region name, for example `ap-south-1`
- Default output format, for example `json`

Verify:

```bash
aws sts get-caller-identity --profile learning
```

## CLI Files

AWS CLI stores config here:

```text
~/.aws/config
~/.aws/credentials
```

Inspect safely:

```bash
aws configure list
aws configure list-profiles
```

Never paste `~/.aws/credentials` into GitHub, chat, screenshots, or notes.

## Default Region

For India-based learning:

```bash
aws configure set region ap-south-1 --profile learning
```

Check available regions:

```bash
aws ec2 describe-regions --output table
```

## Budget Alert

Create a budget in the AWS console first. After that, verify from CLI:

```bash
aws budgets describe-budgets --account-id YOUR_ACCOUNT_ID
```

## First Safe Commands

These commands only read account information:

```bash
aws sts get-caller-identity
aws ec2 describe-regions --output table
aws s3 ls
aws iam get-account-summary
```

## CLI Output Formats

```bash
aws ec2 describe-regions --output json
aws ec2 describe-regions --output table
aws ec2 describe-regions --query "Regions[].RegionName" --output text
```

## Cleanup Habit

After every lab:

```bash
aws resourcegroupstaggingapi get-resources --tag-filters Key=Project,Values=aws-learning
```

If using Terraform:

```bash
terraform plan -destroy
terraform destroy
```
