# Docker And Containers On AWS

The common beginner-to-real-world path is:

1. Build a Docker image locally.
2. Run it locally.
3. Push it to ECR.
4. Run it on ECS/Fargate.
5. Add load balancer, logs, autoscaling, and CI/CD.

## Docker Basics

Build:

```bash
docker build -t demo-app:dev .
```

Run:

```bash
docker run --rm -p 8080:8080 demo-app:dev
```

List:

```bash
docker images
docker ps
docker ps -a
```

Clean local unused objects:

```bash
docker system df
docker image prune
docker container prune
```

## Dockerfile Best Practices

Do:

- Use a small trusted base image.
- Pin versions when practical.
- Copy dependency files before app files to improve cache.
- Use `.dockerignore`.
- Run as non-root if the app supports it.
- Keep one main process per container.

Avoid:

- Secrets in `ENV`, `ARG`, or copied files.
- Huge base images.
- Installing unnecessary packages.
- Using `latest` for production.

Example `.dockerignore`:

```gitignore
.git
.env
node_modules
__pycache__
.venv
*.log
terraform.tfstate
.terraform
```

## ECR - Elastic Container Registry

Create repository:

```bash
aws ecr create-repository \
  --repository-name demo-app \
  --image-scanning-configuration scanOnPush=true \
  --region ap-south-1
```

Get account ID:

```bash
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```

Login Docker to ECR:

```bash
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com
```

Tag and push:

```bash
docker tag demo-app:dev ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com/demo-app:dev
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.ap-south-1.amazonaws.com/demo-app:dev
```

List images:

```bash
aws ecr list-images --repository-name demo-app --region ap-south-1
```

## ECS/Fargate Concepts

Key pieces:

- Cluster: logical group for running services/tasks.
- Task definition: container blueprint.
- Task: running copy of a task definition.
- Service: keeps desired number of tasks running.
- Fargate: serverless container compute.
- ALB: load balancer for public HTTP/HTTPS traffic.
- Task role: AWS permissions for the app.
- Execution role: permissions ECS needs to pull images and write logs.

## ECS Best Practices

- Use Fargate first for learning.
- Store images in ECR.
- Send logs to CloudWatch.
- Use task roles, not access keys inside containers.
- Put private services in private subnets.
- Use ALB for public web apps.
- Configure health checks.
- Set CPU and memory intentionally.
- Use autoscaling for production.

## ECS CLI Discovery Commands

```bash
aws ecs list-clusters
aws ecs list-task-definitions
aws ecs list-services --cluster CLUSTER_NAME
aws ecs describe-services --cluster CLUSTER_NAME --services SERVICE_NAME
aws logs describe-log-groups
```

## Cleanup Commands

ECR:

```bash
aws ecr delete-repository --repository-name demo-app --force --region ap-south-1
```

ECS cleanup depends on what you created:

```bash
aws ecs update-service --cluster CLUSTER_NAME --service SERVICE_NAME --desired-count 0
aws ecs delete-service --cluster CLUSTER_NAME --service SERVICE_NAME --force
aws ecs delete-cluster --cluster CLUSTER_NAME
```

If Terraform created the infrastructure:

```bash
terraform destroy
```
