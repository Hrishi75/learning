# AWS Scenario Interview Questions

## 1. Design a highly available web application on AWS.

Use Route 53 for DNS, CloudFront if global caching is needed, an ALB across at
least two Availability Zones, app servers in private subnets using Auto Scaling
or ECS/Fargate, RDS Multi-AZ for relational data, S3 for static assets, and
CloudWatch alarms/logs. Use security groups to allow only required traffic.

## 2. A website is slow. How would you troubleshoot?

Check CloudWatch metrics for ALB latency, target response time, EC2 CPU/memory,
database performance, error rates, and network issues. Review logs, identify
whether the bottleneck is frontend, app, database, or external dependency, then
scale or optimize the right layer.

## 3. An EC2 instance is not reachable by SSH. What do you check?

Check instance state, public IP, route table, Internet Gateway, security group,
NACL, key pair, OS firewall, SSH service, disk full issues, and system status
checks. Prefer SSM Session Manager if configured.

## 4. A private EC2 instance cannot access the internet. What do you check?

Check route table path to NAT Gateway or NAT instance, NAT public subnet route
to Internet Gateway, security group egress, NACL rules, DNS settings, and
whether a VPC endpoint would be better for AWS service access.

## 5. An S3 bucket became public accidentally. What do you do?

Enable Block Public Access, remove public ACLs and bucket policies, review
CloudTrail, check object access, rotate exposed secrets if any, add AWS Config
or Access Analyzer checks, and prevent recurrence with policy guardrails.

## 6. How would you store application secrets?

Use Secrets Manager for secrets needing rotation, Parameter Store for simpler
configuration/secrets, encrypt with KMS, grant access using IAM roles, and avoid
secrets in Git, images, logs, or Terraform state.

## 7. How would you deploy a Docker app to AWS?

Build the image, scan it, push to ECR, create an ECS task definition, run it on
ECS/Fargate, attach an ALB if public, send logs to CloudWatch, and use an ECS
service for desired count and deployments.

## 8. ECS service tasks keep stopping. How do you debug?

Check ECS service events, stopped task reason, container exit code, CloudWatch
logs, task CPU/memory, image URI, execution role, environment variables,
secrets, health checks, subnet routes, and security groups.

## 9. Terraform apply fails because state is locked. What do you do?

First confirm no other apply is running. If a previous run crashed, inspect the
backend lock record and use `terraform force-unlock` only when you are sure the
lock is stale. Avoid forcing locks casually.

## 10. Someone changed AWS resources manually. What is your response?

Run `terraform plan` to detect drift, understand the manual change, decide
whether to codify it or revert it, and reinforce that Terraform-managed
resources should be changed through code review and pipeline.

## 11. How would you set up Terraform for a team?

Use remote state in S3 with locking, encryption and restricted access, separate
state per environment, code review, CI checks, provider version pinning, a
module strategy, and production approval gates.

## 12. How would you make an application cost-efficient?

Right-size compute, use autoscaling, stop dev resources after hours, use
Savings Plans for steady workloads, lifecycle old S3 data, avoid unnecessary
NAT Gateways and load balancers, set budgets, and review Cost Explorer.

## 13. How do you migrate a static website to AWS?

Use S3 for static hosting or origin storage, CloudFront for CDN and HTTPS,
Route 53 for DNS, ACM for certificates, and restrict direct bucket access using
CloudFront origin access controls.

## 14. How would you protect a production database?

Use private subnets, restrictive security groups, encryption, backups, Multi-AZ,
least-privilege IAM, Secrets Manager for credentials, monitoring, patching, and
tested restore procedures.

## 15. How do you handle disaster recovery?

Define RTO/RPO, back up data, replicate critical assets, use Multi-AZ for high
availability, consider multi-region for stronger DR, automate infrastructure,
and test recovery regularly.

## 16. An ALB returns 502. What do you check?

Check target health, app port, security groups, container/instance logs, target
group protocol/port, health check path, app crash loops, timeout settings, and
whether the backend is listening.

## 17. An ALB returns 503. What do you check?

Check whether the target group has healthy targets, ECS service desired count,
Auto Scaling capacity, health check failures, deployment status, and routing
rules.

## 18. How do you design a secure three-tier VPC?

Use public subnets for ALB, private app subnets for compute, private database
subnets for RDS, route tables per tier, NAT only for needed outbound access,
tight security groups, and no public database exposure.

## 19. How would you use AWS accounts in a company?

Use AWS Organizations with separate accounts for dev, staging, prod, security,
logging, and shared services. Apply SCP guardrails and centralized identity.

## 20. How do you monitor production?

Collect metrics, logs, traces, and audit events. Use CloudWatch alarms, log
retention, dashboards, synthetics or health checks, CloudTrail, and incident
notifications.

## 21. How would you rotate leaked application credentials?

Disable leaked credentials, rotate secrets in Secrets Manager or the source
system, redeploy workloads, inspect logs for misuse, invalidate sessions if
needed, and add prevention controls.

## 22. How do you make S3 suitable for compliance data?

Use encryption, versioning, Object Lock if required, access logging/auditing,
least privilege, Block Public Access, lifecycle retention, and tested restore
processes.

## 23. How do you deploy without downtime?

Use load balancers, health checks, rolling/blue-green/canary deployments,
backward-compatible changes, database migration planning, and fast rollback.

## 24. How would you connect on-premises to AWS?

Use Site-to-Site VPN for encrypted internet connectivity or Direct Connect for
dedicated private connectivity. Use routing, CIDR planning, and security controls
carefully.

## 25. How do you answer "Which AWS service should I use?"

Start from requirements: traffic pattern, data model, latency, compliance,
operations effort, cost, scaling needs, and team skill. Then choose the simplest
managed service that satisfies the constraints.

## 26. How do you prepare for an AWS DevOps interview?

Know IAM, VPC, EC2, S3, RDS, CloudWatch, ECS/ECR, Terraform, Docker, CI/CD,
security best practices, and cost control. Practice explaining real scenarios
with tradeoffs.

## 27. What is your production-readiness checklist?

Security reviewed, least privilege applied, backups enabled, monitoring and
alerts configured, logs retained, scaling tested, rollback planned, costs
estimated, infrastructure in code, and ownership documented.

## 28. How do you handle high traffic suddenly?

Use autoscaling, caching with CloudFront or ElastiCache, queue background work
with SQS, scale databases carefully, protect dependencies, and monitor errors
and latency.

## 29. How would you troubleshoot high AWS bill?

Use Cost Explorer, group by service/region/tag, find unusual spikes, inspect
running resources, check NAT Gateway/data transfer/load balancers/EBS snapshots,
delete unused resources, and add budgets.

## 30. How do you explain AWS simply to a beginner?

AWS is a set of online building blocks for applications: servers, storage,
networks, databases, security, monitoring, and deployment tools. You rent what
you need and automate it for repeatable systems.
