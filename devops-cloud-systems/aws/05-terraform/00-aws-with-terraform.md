# AWS With Terraform

Use Terraform when you want repeatable infrastructure instead of clicking in
the AWS console.

## Project Structure

Good starter layout:

```text
aws-terraform-lab/
  main.tf
  variables.tf
  outputs.tf
  versions.tf
  providers.tf
  terraform.tfvars.example
  README.md
```

Larger layout:

```text
infra/
  modules/
    vpc/
    app/
    database/
  envs/
    dev/
      main.tf
      backend.tf
      terraform.tfvars
    prod/
      main.tf
      backend.tf
      terraform.tfvars
```

## Provider Setup

`versions.tf`:

```hcl
terraform {
  required_version = ">= 1.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

`providers.tf`:

```hcl
provider "aws" {
  region = var.aws_region
}
```

`variables.tf`:

```hcl
variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "ap-south-1"
}
```

Use profile from shell:

```bash
export AWS_PROFILE=dev-admin
terraform init
terraform plan
```

## Basic S3 Bucket Example

`main.tf`:

```hcl
resource "aws_s3_bucket" "learning" {
  bucket = "replace-with-globally-unique-name"

  tags = {
    Project     = "aws-learning"
    Environment = "dev"
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket_public_access_block" "learning" {
  bucket = aws_s3_bucket.learning.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "learning" {
  bucket = aws_s3_bucket.learning.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "learning" {
  bucket = aws_s3_bucket.learning.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

Workflow:

```bash
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

## Remote State Backend

For team-safe work, store state in S3 and use locking.

Create backend resources once:

```bash
aws s3 mb s3://YOUR_TF_STATE_BUCKET --region ap-south-1
aws s3api put-bucket-versioning --bucket YOUR_TF_STATE_BUCKET --versioning-configuration Status=Enabled
aws dynamodb create-table \
  --table-name terraform-locks \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region ap-south-1
```

`backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket         = "YOUR_TF_STATE_BUCKET"
    key            = "dev/app/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

Initialize:

```bash
terraform init
```

## Important Commands

```bash
terraform fmt -recursive
terraform init
terraform validate
terraform plan
terraform apply
terraform output
terraform state list
terraform destroy
```

Advanced:

```bash
terraform plan -out=tfplan
terraform apply tfplan
terraform import aws_s3_bucket.example bucket-name
terraform state show aws_s3_bucket.example
terraform graph
```

## Best Practices

- Use remote state for anything beyond tiny local experiments.
- Never commit `terraform.tfstate`.
- Commit `.terraform.lock.hcl`.
- Use modules only when repetition appears.
- Tag every resource.
- Use separate state per environment.
- Review plans before applying.
- Avoid making manual console changes to Terraform-managed resources.
- Use `lifecycle { prevent_destroy = true }` for critical resources.
- Keep production applies behind code review and CI/CD.

## `.gitignore`

```gitignore
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
crash.log
crash.*.log
override.tf
override.tf.json
*_override.tf
*_override.tf.json
```

Keep `terraform.tfvars.example` in Git and put fake/example values in it.
