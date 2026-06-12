# Compute, Storage, And Networking Interview Q&A

## 1. What is EC2?

EC2 is AWS virtual machine compute. You choose an AMI, instance type, storage,
networking, security group, and run your workload on a server you control.

## 2. What is an AMI?

An Amazon Machine Image is a template for launching EC2 instances. It includes
the operating system and optional software configuration.

## 3. What is an EC2 instance type?

An instance type defines CPU, memory, storage, networking, and hardware
capabilities for an EC2 instance.

## 4. What is EBS?

Elastic Block Store provides persistent block storage volumes for EC2. It is
used like a disk attached to a server.

## 5. What is instance store?

Instance store is temporary storage physically attached to the host. It is fast
but data is lost when the instance stops, terminates, or fails.

## 6. EBS vs EFS?

EBS is block storage attached to EC2, usually one instance at a time. EFS is
managed shared file storage that multiple instances can mount.

## 7. What is Auto Scaling?

Auto Scaling adjusts compute capacity based on desired count or metrics. With
EC2 Auto Scaling Groups, AWS maintains the required number of instances.

## 8. What is an Auto Scaling Group?

An ASG launches and manages a group of EC2 instances across Availability Zones,
maintaining minimum, maximum, and desired capacity.

## 9. What is a launch template?

A launch template defines EC2 launch settings such as AMI, instance type, key
pair, security groups, user data, and IAM instance profile.

## 10. What is user data?

User data is a script or cloud-init configuration that runs when an EC2 instance
boots. It is commonly used for bootstrapping.

## 11. What is Elastic Load Balancing?

ELB distributes traffic across targets such as EC2 instances, containers, or IP
addresses to improve availability and scale.

## 12. ALB vs NLB?

ALB works at Layer 7 and supports HTTP/HTTPS routing, host/path rules, and
application features. NLB works at Layer 4 for high-performance TCP/UDP traffic.

## 13. What is S3?

S3 is object storage. It stores data as objects inside buckets and is used for
backups, logs, static assets, data lakes, and Terraform state.

## 14. Is S3 a filesystem?

No. S3 is object storage, not a traditional filesystem. It has buckets, objects,
keys, metadata, and APIs rather than normal block-level file operations.

## 15. What is an S3 bucket?

An S3 bucket is a globally unique container for objects in a Region.

## 16. How do you secure an S3 bucket?

Block public access, disable ACLs unless required, use least-privilege bucket
policies, enable encryption, enable versioning for important data, and monitor
access with CloudTrail or S3 logs.

## 17. What is S3 versioning?

Versioning keeps multiple versions of an object. It helps recover from
accidental deletion or overwrite.

## 18. What is an S3 lifecycle policy?

A lifecycle policy transitions or expires objects based on age or rules. It is
used for cost optimization and retention control.

## 19. What is S3 Object Lock?

Object Lock can prevent deletion or modification for a retention period. It is
used for compliance and write-once-read-many style protection.

## 20. What is a VPC?

A VPC is a logically isolated virtual network in AWS where you define CIDR
ranges, subnets, route tables, gateways, and network controls.

## 21. What is a subnet?

A subnet is a range of IP addresses inside a VPC, tied to one Availability Zone.

## 22. Public subnet vs private subnet?

A public subnet has a route to an Internet Gateway. A private subnet does not
allow direct inbound internet access and usually reaches the internet through
NAT or VPC endpoints.

## 23. What is an Internet Gateway?

An Internet Gateway allows resources in public subnets to communicate with the
internet when route tables and public IPs allow it.

## 24. What is a NAT Gateway?

A NAT Gateway lets instances in private subnets initiate outbound internet
connections without allowing direct inbound internet access.

## 25. What is a route table?

A route table controls where network traffic from a subnet or gateway is sent.

## 26. What is a Security Group?

A Security Group is a stateful virtual firewall for resources like EC2 and load
balancers. Return traffic is automatically allowed.

## 27. What is a Network ACL?

A NACL is a stateless subnet-level network filter. Both inbound and outbound
rules must explicitly allow traffic.

## 28. Security Group vs NACL?

Security Groups are stateful and attached to resources. NACLs are stateless and
attached to subnets. Security Groups are used more commonly for workload access
control.

## 29. What is a VPC endpoint?

A VPC endpoint lets private resources connect to supported AWS services without
using the public internet.

## 30. Gateway endpoint vs interface endpoint?

Gateway endpoints are used for S3 and DynamoDB route table integration.
Interface endpoints use private IPs and AWS PrivateLink for many services.

## 31. What is Route 53?

Route 53 is AWS DNS and domain routing service. It supports hosted zones,
records, health checks, and routing policies.

## 32. What is CloudFront?

CloudFront is a CDN that caches content at edge locations to reduce latency and
offload origin servers.

## 33. How do you design a highly available web app on AWS?

Use multiple Availability Zones, an ALB, Auto Scaling Group or ECS service,
private app subnets, health checks, CloudWatch alarms, and managed database
services with backups/Multi-AZ where needed.

## 34. How do you reduce EC2 cost?

Right-size instances, stop unused dev instances, use Auto Scaling, choose
Savings Plans or Reserved Instances for steady workloads, use Spot for
fault-tolerant workloads, and monitor with Cost Explorer.

## 35. How do you troubleshoot an EC2 instance that cannot be reached?

Check instance state, system status checks, security groups, NACLs, route
tables, public/private IP, key pair, OS firewall, user data logs, and whether
SSM Session Manager is available.
