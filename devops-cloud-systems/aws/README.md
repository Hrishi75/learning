# AWS Learning Path

A clean, practical path to learn AWS from basics to advanced DevOps usage.
Read the files in order, run commands in your own terminal, and keep security
habits from day one.

> Cost rule: AWS can charge money. Start with Free Tier-aware services, set
> budgets/alerts, and destroy lab resources after practice.

## How To Use This Folder

1. Read `01-foundations/` first to understand the cloud model.
2. Configure your tools from `02-setup/`.
3. Learn services from `03-core-services/`.
4. Keep `04-security/` open while building anything.
5. Use `05-terraform/` when you are ready for Infrastructure as Code.
6. Use `06-docker-containers/` for Docker, ECR, ECS, and container deployment.
7. Build the labs in `07-projects/`.
8. Use `cheatsheets/` for quick command recall.

## Folder Map

| Folder | Purpose |
|--------|---------|
| `01-foundations/` | Cloud concepts, AWS global infrastructure, pricing basics |
| `02-setup/` | AWS account, IAM Identity Center, CLI, Terraform, Docker setup |
| `03-core-services/` | EC2, VPC, S3, IAM, RDS, CloudWatch, Route 53, Lambda |
| `04-security/` | IAM, least privilege, network security, secrets, logging, audit |
| `05-terraform/` | AWS provider, remote state, modules, environment structure |
| `06-docker-containers/` | Docker basics, ECR image push, ECS/Fargate deployment |
| `07-projects/` | Hands-on mini projects from beginner to advanced |
| `cheatsheets/` | AWS CLI commands and security checklist |

## Recommended Practice Order

1. Account setup + CLI login
2. S3 bucket lab
3. EC2 + security group lab
4. VPC basics lab
5. Terraform S3 backend lab
6. Docker image to ECR lab
7. ECS/Fargate container lab
8. Monitoring + logs + budget alerts
9. CI/CD deployment pipeline
10. Multi-environment Terraform project

## Official References

- AWS CLI install guide: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Docker Engine on Ubuntu: https://docs.docker.com/engine/install/ubuntu/
- Terraform install guide: https://developer.hashicorp.com/terraform/install
- Terraform AWS provider: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
