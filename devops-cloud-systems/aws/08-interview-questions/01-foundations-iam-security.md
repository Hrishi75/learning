# Foundations, IAM, And Security Interview Q&A

## 1. What is AWS?

AWS is a cloud provider that offers on-demand compute, storage, networking,
database, analytics, security, and DevOps services. Instead of buying servers,
you rent resources and pay for what you use.

## 2. What is cloud computing?

Cloud computing is the delivery of computing resources over the internet with
on-demand provisioning, elasticity, measured billing, and managed infrastructure.

## 3. What are the main cloud service models?

- IaaS: infrastructure like EC2, VPC, EBS.
- PaaS: managed platforms like Elastic Beanstalk or managed databases.
- SaaS: complete software delivered as a service.

## 4. What is the shared responsibility model?

AWS secures the infrastructure of the cloud. The customer secures what they run
in the cloud, such as IAM permissions, data, operating systems on EC2, network
rules, application code, and secrets.

## 5. What is an AWS Region?

A Region is a geographic area where AWS hosts services. Each Region contains
multiple isolated Availability Zones.

## 6. What is an Availability Zone?

An Availability Zone is one or more isolated data centers inside a Region. AZs
are connected with low-latency networking and help design highly available
systems.

## 7. How do you choose an AWS Region?

Consider latency to users, service availability, compliance, data residency,
cost, and disaster recovery needs.

## 8. What is IAM?

IAM is AWS Identity and Access Management. It controls who can authenticate and
what actions they are authorized to perform.

## 9. What is the difference between authentication and authorization?

Authentication proves who you are. Authorization decides what you are allowed to
do after identity is verified.

## 10. What is an IAM user?

An IAM user is an identity with long-term credentials. It is less preferred for
humans in modern setups because federated access and temporary credentials are
safer.

## 11. What is an IAM group?

An IAM group is a collection of IAM users. Policies attached to the group apply
to all users in that group.

## 12. What is an IAM role?

An IAM role is an identity that can be assumed by users, services, or workloads.
It provides temporary credentials and is preferred over long-lived access keys.

## 13. What is an IAM policy?

An IAM policy is a JSON document that defines allowed or denied actions on AWS
resources, optionally under conditions.

## 14. What is least privilege?

Least privilege means granting only the permissions needed for a specific task,
on the specific resources required, for the required time.

## 15. Why should you avoid root user usage?

The root user has full account access. If compromised, the entire account is at
risk. Use root only for account-level tasks and protect it with MFA.

## 16. Why is MFA important?

MFA adds a second factor beyond password or access key. It reduces the risk of
account takeover if credentials are leaked.

## 17. What is IAM Identity Center?

IAM Identity Center provides centralized workforce access to AWS accounts and
applications, commonly with SSO and temporary role-based access.

## 18. What are temporary credentials?

Temporary credentials are short-lived access keys, secret keys, and session
tokens issued by AWS STS when assuming a role or using federation.

## 19. What is AWS STS?

AWS Security Token Service issues temporary security credentials, commonly used
for role assumption, federation, and cross-account access.

## 20. What is a trust policy?

A trust policy defines who or what can assume an IAM role. A permissions policy
defines what the role can do after it is assumed.

## 21. What is cross-account access?

Cross-account access allows an identity in one AWS account to access resources
or assume a role in another account, usually controlled by trust and permission
policies.

## 22. What is an IAM permission boundary?

A permissions boundary sets the maximum permissions an identity can receive. It
does not grant permissions by itself.

## 23. What is a Service Control Policy?

An SCP is an AWS Organizations policy that sets maximum allowed permissions for
accounts or organizational units. It does not grant permissions by itself.

## 24. What is AWS KMS?

AWS Key Management Service manages encryption keys used by services and
applications. It supports AWS-managed and customer-managed keys.

## 25. What is Secrets Manager?

Secrets Manager stores, encrypts, retrieves, and can rotate secrets such as
database passwords and API keys.

## 26. What is SSM Parameter Store?

Parameter Store stores configuration values and secrets. SecureString parameters
can be encrypted with KMS.

## 27. Secrets Manager vs Parameter Store?

Secrets Manager is better for secret rotation and managed secret lifecycle.
Parameter Store is useful for app configuration and simpler secret storage.

## 28. What is CloudTrail?

CloudTrail records AWS API activity. It is used for audit, security
investigation, and tracking who changed what.

## 29. What is GuardDuty?

GuardDuty is a threat detection service that analyzes AWS data sources for
potentially malicious or unauthorized activity.

## 30. How do you secure an AWS account before using it?

Enable root MFA, avoid root for daily work, configure IAM Identity Center or
admin roles, create budgets, enable CloudTrail, use least privilege, and review
public access regularly.

## 31. What is the difference between identity-based and resource-based policies?

Identity-based policies attach to users, groups, or roles. Resource-based
policies attach directly to resources, such as S3 bucket policies or KMS key
policies.

## 32. What is explicit deny?

An explicit deny overrides any allow. It is useful for guardrails such as
blocking public access, blocking actions outside approved regions, or enforcing
encryption.

## 33. How would you investigate leaked AWS credentials?

Disable or delete the key, rotate affected secrets, check CloudTrail for API
activity, inspect created resources, review IAM permissions, and add controls
to prevent recurrence.

## 34. Why should access keys not be stored in code?

Code repositories, logs, images, and backups can leak. Use IAM roles, SSO,
OIDC, or secret stores instead.

## 35. What is AWS Well-Architected?

It is a framework for reviewing cloud workloads against best practices across
operational excellence, security, reliability, performance efficiency, cost
optimization, and sustainability.
