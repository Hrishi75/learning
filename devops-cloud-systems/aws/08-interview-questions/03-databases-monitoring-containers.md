# Databases, Monitoring, And Containers Interview Q&A

## 1. What is RDS?

RDS is a managed relational database service for engines such as PostgreSQL,
MySQL, MariaDB, Oracle, SQL Server, and Aurora.

## 2. Why use RDS instead of running a database on EC2?

RDS reduces operational work by managing backups, patching, monitoring,
replication options, and availability features. EC2 gives more control but more
maintenance responsibility.

## 3. What is RDS Multi-AZ?

Multi-AZ creates a standby database in another Availability Zone for high
availability. If the primary fails, AWS can fail over to the standby.

## 4. What is a read replica?

A read replica is an asynchronously replicated copy used to scale read traffic
or support reporting workloads.

## 5. Multi-AZ vs read replica?

Multi-AZ is mainly for high availability and failover. Read replicas are mainly
for read scaling and can also help with disaster recovery.

## 6. What is Amazon Aurora?

Aurora is an AWS-designed relational database compatible with MySQL or
PostgreSQL, built for cloud performance, availability, and managed operations.

## 7. What is DynamoDB?

DynamoDB is a managed NoSQL key-value and document database designed for high
scale and low-latency access.

## 8. RDS vs DynamoDB?

RDS is relational and SQL-based, good for joins and transactions. DynamoDB is
NoSQL, good for predictable access patterns, massive scale, and low latency.

## 9. What is a DynamoDB partition key?

A partition key is used to distribute items across partitions. Good key design
is critical for performance and avoiding hot partitions.

## 10. What is DynamoDB sort key?

A sort key orders items with the same partition key and enables range queries.

## 11. What is ElastiCache?

ElastiCache is a managed in-memory caching service using Redis-compatible or
Memcached engines to reduce database load and improve latency.

## 12. What is CloudWatch?

CloudWatch collects metrics, logs, events, alarms, and dashboards for AWS
resources and applications.

## 13. What are CloudWatch metrics?

Metrics are time-series data points such as CPU utilization, request count,
latency, or error rate.

## 14. What are CloudWatch Logs?

CloudWatch Logs stores and searches log events from applications, services, and
AWS resources.

## 15. What is a CloudWatch alarm?

An alarm watches a metric and triggers actions when the metric crosses a
threshold.

## 16. CloudWatch vs CloudTrail?

CloudWatch is operational monitoring. CloudTrail is audit logging for AWS API
activity.

## 17. What is EventBridge?

EventBridge routes events from AWS services, SaaS providers, and custom apps to
targets such as Lambda, Step Functions, or queues.

## 18. What is SNS?

SNS is a publish/subscribe messaging service used for notifications and fan-out
messaging.

## 19. What is SQS?

SQS is a managed queue service that decouples producers and consumers and helps
smooth traffic spikes.

## 20. SNS vs SQS?

SNS pushes messages to subscribers. SQS stores messages for consumers to poll.
They are often used together for fan-out with buffering.

## 21. What is Lambda?

Lambda runs code without managing servers. You pay based on requests and
execution duration.

## 22. When should you not use Lambda?

Avoid Lambda for long-running workloads beyond service limits, workloads needing
special host-level control, or applications where container/server design is
simpler and cheaper.

## 23. What is ECR?

ECR is AWS managed container image registry. It stores Docker/OCI images and
integrates with IAM, ECS, EKS, and image scanning features.

## 24. What is ECS?

ECS is AWS managed container orchestration. It deploys, manages, and scales
containerized applications.

## 25. What is Fargate?

Fargate is serverless compute for containers. You run ECS or EKS workloads
without managing EC2 container hosts.

## 26. ECS on EC2 vs ECS on Fargate?

ECS on EC2 gives more control over instances, pricing, and host configuration.
Fargate removes server management and is simpler for many workloads.

## 27. What is an ECS cluster?

An ECS cluster is a logical grouping where tasks and services run.

## 28. What is an ECS task definition?

A task definition is the blueprint for containers, CPU, memory, ports,
environment variables, logging, and IAM roles.

## 29. What is an ECS task?

A task is a running instance of a task definition.

## 30. What is an ECS service?

An ECS service maintains a desired number of running tasks and integrates with
load balancers, deployments, and autoscaling.

## 31. ECS task role vs execution role?

The task role gives permissions to the application container. The execution
role lets ECS pull images from ECR and write logs to CloudWatch.

## 32. How do containers on AWS get credentials securely?

Use IAM roles, such as ECS task roles or IRSA for EKS. Do not store access keys
inside images or environment files committed to Git.

## 33. What is image scanning in ECR?

Image scanning checks container images for known vulnerabilities so teams can
fix risky dependencies or base images.

## 34. What is a container health check?

A health check verifies that a container or application endpoint is working.
ECS or a load balancer can replace unhealthy tasks.

## 35. How do you troubleshoot an ECS service not starting?

Check service events, task stopped reason, task definition, container logs,
security groups, subnet routing, IAM execution role, ECR image URI, CPU/memory,
and target group health checks.
