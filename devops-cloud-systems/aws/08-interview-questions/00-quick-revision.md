# AWS Interview Quick Revision

## Must-Know One-Liners

- AWS Region: a physical geographic area with multiple Availability Zones.
- Availability Zone: isolated data center location inside a Region.
- IAM: controls authentication and authorization in AWS.
- IAM role: assumable identity with temporary credentials.
- Least privilege: grant only required permissions for a task.
- VPC: isolated virtual network for AWS resources.
- Public subnet: subnet with route to an Internet Gateway.
- Private subnet: subnet without direct inbound internet access.
- Security Group: stateful virtual firewall attached to resources.
- NACL: stateless subnet-level network filter.
- S3: object storage for files, logs, backups, static assets, and state.
- EC2: virtual machine service.
- EBS: block storage for EC2.
- EFS: shared managed file storage.
- ALB: Layer 7 HTTP/HTTPS load balancer.
- NLB: Layer 4 TCP/UDP load balancer.
- Auto Scaling Group: maintains desired number of EC2 instances.
- RDS: managed relational database service.
- DynamoDB: managed NoSQL key-value/document database.
- CloudWatch: metrics, logs, alarms, dashboards.
- CloudTrail: AWS API activity audit log.
- ECR: private container image registry.
- ECS: managed container orchestration service.
- Fargate: serverless compute for containers.
- Terraform state: mapping between code and real infrastructure.
- Remote state: state stored outside local machine, usually S3 for AWS.

## Best Answers To Repeat Often

Why prefer IAM roles over access keys?

- Roles provide temporary credentials, reduce secret leakage risk, and are the
  standard for AWS services and federated access.

How do you secure an S3 bucket?

- Block public access, disable ACLs unless required, use bucket policies, enable
  encryption, enable versioning for important data, audit with CloudTrail/S3
  access logs, and apply least privilege.

How do you design a secure VPC?

- Use public subnets only for entrypoints like load balancers, private subnets
  for app/database tiers, tight security groups, route tables per tier, and VPC
  endpoints where possible.

What is the difference between CloudWatch and CloudTrail?

- CloudWatch is for metrics, logs, alarms, and operational visibility.
  CloudTrail records AWS API activity for auditing and investigation.

What is Terraform remote state?

- Remote state stores Terraform state in a shared backend, such as S3, so teams
  can collaborate safely. Locking prevents simultaneous conflicting updates.

What are the AWS Well-Architected pillars?

- Operational excellence, security, reliability, performance efficiency, cost
  optimization, and sustainability.

## Interview Answer Formula

Use this pattern:

```text
Definition -> Why it matters -> Example -> Best practice -> Tradeoff
```

Example:

```text
An IAM role is an identity that can be assumed to receive temporary credentials.
It matters because services and users do not need long-lived access keys.
For example, an ECS task can assume a task role to read from S3.
Best practice is least privilege with only required actions/resources.
The tradeoff is that role trust policies and permission policies must be managed carefully.
```
