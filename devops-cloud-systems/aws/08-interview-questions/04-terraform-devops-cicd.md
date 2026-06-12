# Terraform, DevOps, Docker, And CI/CD Interview Q&A

## 1. What is Infrastructure as Code?

Infrastructure as Code means defining infrastructure in version-controlled files
instead of creating resources manually in a console.

## 2. What is Terraform?

Terraform is an IaC tool that uses providers to manage infrastructure resources
across cloud platforms and services.

## 3. What is a Terraform provider?

A provider is a plugin that lets Terraform interact with an API, such as AWS,
Docker, Kubernetes, or GitHub.

## 4. What is a Terraform resource?

A resource is an infrastructure object managed by Terraform, such as an S3
bucket, VPC, EC2 instance, or IAM role.

## 5. What is Terraform state?

State is Terraform's record of resources it manages and their attributes. It
maps Terraform configuration to real infrastructure.

## 6. Why is Terraform state sensitive?

State can contain resource details and sometimes sensitive values. It should be
stored securely, encrypted, access-controlled, and not committed to Git.

## 7. What is remote state?

Remote state stores Terraform state in a shared backend such as S3. It enables
team collaboration and safer automation.

## 8. Why use state locking?

State locking prevents multiple Terraform runs from changing the same state at
the same time, avoiding corruption or conflicting updates.

## 9. What is `terraform init`?

It initializes the working directory, downloads providers/modules, and configures
the backend.

## 10. What is `terraform plan`?

It shows proposed infrastructure changes before applying them.

## 11. What is `terraform apply`?

It executes the planned changes and updates state.

## 12. What is `terraform destroy`?

It removes resources managed by the Terraform configuration and updates state.

## 13. What is `terraform import`?

It brings an existing real resource under Terraform state management. You still
need matching configuration afterward.

## 14. What is drift?

Drift is when real infrastructure differs from Terraform configuration or state,
often because someone changed resources manually.

## 15. How do you handle drift?

Run `terraform plan`, understand the difference, decide whether to update code
or revert the manual change, and avoid console edits for managed resources.

## 16. What is a Terraform module?

A module is a reusable group of Terraform configuration files. Modules help
standardize repeated infrastructure patterns.

## 17. Root module vs child module?

The root module is the current working configuration. Child modules are called
from the root or other modules.

## 18. Why should provider configuration usually stay in the root module?

It keeps provider setup centralized. Child modules should generally receive
provider configuration from the root module.

## 19. How do you manage dev and prod in Terraform?

Use separate state per environment, separate variable files or directories,
clear naming/tags, and review/approval for production applies.

## 20. What should be in `.gitignore` for Terraform?

Ignore `.terraform/`, state files, crash logs, local override files, and real
`.tfvars` containing secrets. Commit `.terraform.lock.hcl`.

## 21. What is Docker?

Docker packages applications and dependencies into images that run as containers
consistently across environments.

## 22. What is a Docker image?

A Docker image is an immutable package containing filesystem layers, runtime
dependencies, and metadata used to start containers.

## 23. What is a Docker container?

A container is a running instance of an image.

## 24. What is a Dockerfile?

A Dockerfile is a set of instructions to build a container image.

## 25. What is `.dockerignore`?

`.dockerignore` prevents unnecessary or sensitive files from being sent into the
Docker build context.

## 26. Why should secrets not be baked into images?

Image layers can be inspected, copied, cached, and pushed to registries. Secrets
inside images are difficult to fully remove and can leak broadly.

## 27. How do you push a Docker image to ECR?

Create an ECR repository, authenticate Docker with `aws ecr get-login-password`,
tag the image with the ECR repository URI, and push it.

## 28. What is CI/CD?

CI validates code changes with automated builds and tests. CD automates delivery
or deployment to environments.

## 29. How do you deploy to AWS from GitHub Actions securely?

Use OIDC federation to assume an AWS role, avoid long-lived AWS keys in GitHub
secrets, restrict role trust policy, and grant least privilege.

## 30. What is blue/green deployment?

Blue/green keeps two environments or task sets. Traffic shifts from the current
version to the new version, allowing rollback if issues appear.

## 31. What is rolling deployment?

A rolling deployment gradually replaces old instances or tasks with new ones
while keeping the service available.

## 32. What is canary deployment?

A canary deployment sends a small percentage of traffic to the new version first
and increases traffic if metrics remain healthy.

## 33. What should a deployment pipeline check before production?

Formatting, tests, security scans, Terraform plan, image vulnerability scans,
policy checks, manual approval, and rollback strategy.

## 34. How do you reduce deployment risk?

Use small changes, automated tests, health checks, staged environments,
immutable artifacts, gradual rollout, monitoring, and rollback plans.

## 35. What is immutable infrastructure?

Immutable infrastructure replaces servers or containers instead of modifying
them in place. This makes deployments more repeatable and easier to roll back.
