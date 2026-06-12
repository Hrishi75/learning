# Local Tooling Setup

These tools are enough for most AWS DevOps practice:

- AWS CLI v2
- Terraform
- Docker
- Git
- A code editor

The commands below assume Ubuntu or WSL Ubuntu.

## System Update

```bash
sudo apt-get update
sudo apt-get install -y curl unzip gnupg lsb-release ca-certificates git
```

## Install AWS CLI v2

Official AWS Linux installer:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

Update later:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -u awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

Best practice:

- Prefer AWS CLI v2.
- Avoid random third-party install scripts.
- Use `aws --version` after install.
- Do not store access keys in shared screenshots, Git repos, or notes.

## Install Terraform

HashiCorp apt repository method:

```bash
sudo apt-get update
sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt-get update
sudo apt-get install -y terraform
terraform version
terraform -install-autocomplete
```

Best practice:

- Pin provider versions in every Terraform project.
- Commit `.terraform.lock.hcl`.
- Do not commit `.terraform/` or `terraform.tfstate`.

## Install Docker Engine

Docker official apt repository method:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo ${UBUNTU_CODENAME:-$VERSION_CODENAME}) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world
```

Optional non-root Docker usage:

```bash
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

Best practice:

- Use small base images.
- Keep `.dockerignore`.
- Do not bake secrets into images.
- Scan images before pushing to a registry.

## Useful Verification Commands

```bash
git --version
aws --version
terraform version
docker version
docker compose version
```

## Suggested Local Folder Layout

```text
~/aws-labs/
  01-s3/
  02-ec2/
  03-vpc/
  04-terraform-s3/
  05-docker-ecr/
  06-ecs-fargate/
```
