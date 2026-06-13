# Terraform Learning Guide (WSL / Linux)

A step-by-step, hands-on path to learn Terraform from zero. Run every command
yourself inside WSL. Each section says **what** you do and **why** it matters,
with security and best practices baked in.

> **Where to keep your code (important):**
> Working from `/mnt/d/learning/...` (a Windows drive) inside WSL is **slow** and
> causes file-permission warnings. For real practice, copy projects into WSL's
> native filesystem, e.g. `~/terraform-labs/`. You can keep this guide on the
> Windows side and write code in WSL home.

---

## Table of Contents

0. [What Terraform is (concepts)](#phase-0--concepts)
1. [Install Terraform on WSL](#phase-1--install-on-wsl)
2. [First project — local provider (no cloud needed)](#phase-2--first-project)
3. [Core workflow: init / plan / apply / destroy](#phase-3--core-workflow)
4. [Variables, outputs, locals](#phase-4--variables-outputs-locals)
5. [State — what it is, why it matters, how to protect it](#phase-5--state)
6. [Remote state backend (team-safe)](#phase-6--remote-backend)
7. [A real provider (Docker, runs locally)](#phase-7--docker-provider)
8. [Modules — reusable building blocks](#phase-8--modules)
9. [Security & secrets best practices](#phase-9--security)
10. [Quality tooling: fmt, validate, tflint, checkov](#phase-10--quality-tooling)
11. [Workspaces & environments](#phase-11--workspaces)
12. [Git hygiene & .gitignore](#phase-12--git)
13. [Cheat sheet](#cheat-sheet)

---

## Phase 0 — Concepts

**Terraform** = Infrastructure as Code (IaC). You describe infra (servers,
networks, containers, DNS...) in `.tf` files. Terraform makes reality match
the files.

Key words:
- **Provider** — plugin that talks to a platform (AWS, Azure, Docker, local files).
- **Resource** — one thing Terraform manages (a VM, a file, a container).
- **State** — Terraform's record of what it created (`terraform.tfstate`).
- **Plan** — preview of changes before applying.
- **Declarative** — you say the *desired end state*, not the steps. Terraform
  computes the diff.

Mental model: `desired (your .tf) - current (state) = plan (changes to make)`.

---

## Phase 1 — Install on WSL

Why this method: HashiCorp's signed apt repo gives verified packages and easy
updates. Never `curl | bash` random scripts for infra tools.

```bash
# 1. Update + install dependencies
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl

# 2. Add HashiCorp GPG key (verifies package authenticity)
wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# 3. Add the repo, pinned to that signing key
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
  https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list

# 4. Install Terraform
sudo apt-get update && sudo apt-get install -y terraform

# 5. Verify
terraform version
terraform -install-autocomplete   # one-time: enables tab completion (reopen shell after)
```

Expected: `Terraform v1.x.x on linux_amd64`.

---

## Phase 2 — First Project

Goal: learn the workflow with zero cloud risk using the built-in `local`
provider (it just writes files).

```bash
mkdir -p ~/terraform-labs/01-hello && cd ~/terraform-labs/01-hello
```

Create `main.tf`:

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"   # pin: allow 2.5.x, block surprise 3.0 breakage
    }
  }
}

resource "local_file" "hello" {
  filename = "${path.module}/hello.txt"
  content  = "Hello from Terraform!\n"
}
```

Why pin versions: reproducible builds. Same code = same provider = same result
months later.

---

## Phase 3 — Core Workflow

These 5 commands are 90% of daily Terraform.

```bash
terraform init      # download providers, set up .terraform/ (run once per project / on provider change)
terraform fmt       # auto-format your .tf files to canonical style
terraform validate  # check syntax + internal consistency (no cloud calls)
terraform plan      # preview: what will be created/changed/destroyed
terraform apply     # do it (asks "yes" to confirm)
```

Read the plan symbols every time:
- `+` create
- `~` modify in place
- `-` destroy
- `-/+` replace (destroy then create) — **watch for data loss**

Inspect and clean up:

```bash
terraform show          # human-readable current state
terraform state list    # list managed resources
terraform destroy       # tear everything down (asks "yes")
```

**Best practice:** never edit infra by hand outside Terraform ("click-ops").
It causes *drift* — state and reality disagree. Always change the `.tf` and
re-apply.

---

## Phase 4 — Variables, Outputs, Locals

Stop hardcoding. Make config reusable.

`variables.tf`:
```hcl
variable "greeting" {
  description = "Text written to the file"
  type        = string
  default     = "Hello from a variable!"
}

variable "filename" {
  description = "Output file name"
  type        = string
  default     = "greeting.txt"
}
```

`main.tf` (use them):
```hcl
locals {
  full_content = "${var.greeting} (generated ${timestamp()})\n"
}

resource "local_file" "greeting" {
  filename = "${path.module}/${var.filename}"
  content  = local.full_content
}
```

`outputs.tf`:
```hcl
output "file_path" {
  description = "Where the file was written"
  value       = local_file.greeting.filename
}
```

Set variables (precedence low → high):
```bash
# default in variables.tf  <  terraform.tfvars  <  -var  <  TF_VAR_ env
terraform apply -var="greeting=Hi there"
TF_VAR_greeting="From env" terraform apply
```

- **variable** = input you pass in.
- **local** = computed value reused inside the config (DRY).
- **output** = value Terraform prints / exposes to other modules.

---

## Phase 5 — State

`terraform.tfstate` is the heart. It maps your `.tf` resources to real-world
IDs.

**Critical security facts:**
- State is **plaintext JSON** and can contain **secrets** (passwords, keys,
  generated tokens).
- **Never commit `*.tfstate` to git.** (See Phase 12 .gitignore.)
- Locally it's fine for learning; for any team/cloud work use a **remote
  backend** with encryption + locking (Phase 6).

Useful (careful) commands:
```bash
terraform state list                 # what's tracked
terraform state show <resource>      # details of one resource
terraform refresh                    # sync state with real world (read-only-ish)
```

Avoid `terraform state rm` / `import` until you understand them — they edit
state directly and can orphan or duplicate resources.

---

## Phase 6 — Remote Backend

Why: local state breaks teamwork (no sharing, no locking → two people apply at
once → corruption). Remote backends fix this.

Example (AWS S3 + DynamoDB lock). Don't run unless you have an AWS account and
understand it may incur tiny costs.

```hcl
terraform {
  backend "s3" {
    bucket         = "my-tf-state-bucket"     # must already exist
    key            = "labs/hello/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-locks"        # provides state locking
    encrypt        = true                     # encrypt state at rest (do not omit)
  }
}
```

Best practices for the state bucket:
- Enable **versioning** (recover from bad applies).
- Enable **encryption** (`encrypt = true` + bucket SSE).
- **Block all public access.**
- Restrict access with least-privilege IAM.
- Use **DynamoDB locking** so concurrent applies can't corrupt state.

Free/local alternative to learn backends without a cloud: keep using local
backend, or try a `terraform_remote_state` exercise later.

---

## Phase 7 — Docker Provider

A real provider that runs on your machine (free, no cloud). Needs Docker.

```bash
# Install Docker in WSL (or use Docker Desktop with WSL integration)
sudo apt-get install -y docker.io
sudo service docker start
sudo usermod -aG docker $USER     # then reopen shell so you don't need sudo
docker run hello-world            # verify
```

Project `~/terraform-labs/02-docker/main.tf`:
```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:1.27-alpine"   # pin tag, never use :latest in IaC
  keep_locally = false
}

resource "docker_container" "web" {
  name  = "tf-nginx"
  image = docker_image.nginx.image_id
  ports {
    internal = 80
    external = 8080
  }
}
```

```bash
terraform init && terraform plan && terraform apply
curl http://localhost:8080        # nginx welcome page
terraform destroy                 # clean up
```

Why `:latest` is banned: it's a moving target. A re-apply months later silently
pulls a different image → non-reproducible, possible breakage. Always pin.

---

## Phase 8 — Modules

A **module** = a folder of `.tf` files you reuse with different inputs. Keeps
code DRY and consistent.

Structure:
```
03-modules/
├── main.tf            # root: calls the module
└── modules/
    └── webfile/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

`modules/webfile/variables.tf`:
```hcl
variable "name"    { type = string }
variable "content" { type = string }
```

`modules/webfile/main.tf`:
```hcl
resource "local_file" "this" {
  filename = "${path.module}/${var.name}.txt"
  content  = var.content
}
```

`modules/webfile/outputs.tf`:
```hcl
output "path" { value = local_file.this.filename }
```

Root `main.tf`:
```hcl
module "page_a" {
  source  = "./modules/webfile"
  name    = "page_a"
  content = "Content A"
}

module "page_b" {
  source  = "./modules/webfile"
  name    = "page_b"
  content = "Content B"
}

output "a_path" { value = module.page_a.path }
```

Best practices:
- One module = one clear responsibility.
- Pin module versions when sourcing from a registry/git
  (`source = "git::...//mod?ref=v1.2.0"`).
- Don't over-modularize early; extract a module once you copy-paste twice.

---

## Phase 9 — Security

Treat secrets and access as first-class. The biggest IaC risks are leaked
secrets and over-broad permissions.

**Secrets:**
- **Never** hardcode passwords/keys/tokens in `.tf` or `.tfvars` that get
  committed.
- Mark sensitive variables:
  ```hcl
  variable "db_password" {
    type      = string
    sensitive = true   # hides value in plan/apply output
  }
  ```
- Pull secrets from a manager (AWS Secrets Manager, HashiCorp Vault, SSM
  Parameter Store) via data sources — don't store them in code.
- Remember: secrets can still land in **state** (plaintext). Protect state
  (encrypted remote backend) accordingly.

**Credentials:**
- Never put cloud keys in `.tf`. Use env vars / CLI profiles / OIDC.
  ```bash
  # AWS example — credentials live outside Terraform
  export AWS_PROFILE=learning
  aws configure --profile learning   # stores in ~/.aws, not in your repo
  ```
- Use **least-privilege** IAM for the identity Terraform runs as.

**Provider & module supply chain:**
- Pin provider **and** module versions.
- Commit `.terraform.lock.hcl` (the dependency lock) to git — guarantees
  everyone gets identical provider versions/checksums.

**Review discipline:**
- Always read `terraform plan` before `apply`. Watch for `-/+` (replace) and
  `-` (destroy) on anything stateful.

---

## Phase 10 — Quality Tooling

Catch problems before they hit infra.

```bash
terraform fmt -recursive   # consistent formatting across all files
terraform validate         # syntax + config consistency
```

Install extra linters/scanners:
```bash
# tflint — catches likely errors & enforces best practices
curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
tflint --init && tflint

# checkov — security/compliance scanner for IaC
pip install --user checkov     # needs python3 + pip
checkov -d .
```

> Note: piping an install script to bash is a supply-chain risk. The tflint
> command above is the project's official installer; for stricter control,
> download the release binary + verify its checksum instead.

What each finds:
- **fmt/validate** — style + syntax.
- **tflint** — provider-specific mistakes, deprecated usage, naming rules.
- **checkov** — misconfigurations (open security groups, unencrypted storage,
  public buckets).

---

## Phase 11 — Workspaces

Lightweight way to keep separate states for the same code (e.g. dev vs prod).

```bash
terraform workspace list
terraform workspace new dev
terraform workspace new prod
terraform workspace select dev
terraform workspace show
```

Use `terraform.workspace` in code:
```hcl
resource "local_file" "env" {
  filename = "${path.module}/${terraform.workspace}.txt"
  content  = "Environment: ${terraform.workspace}\n"
}
```

Caveat: workspaces are good for small/learning setups. For real prod isolation,
many teams prefer **separate directories/backends per environment** (stronger
blast-radius separation). Learn workspaces first, graduate later.

---

## Phase 12 — Git

Never commit state or secrets. Create `.gitignore` in each Terraform project
(or repo root):

```gitignore
# Terraform
.terraform/             # downloaded providers/modules (large, machine-specific)
*.tfstate               # STATE — may contain secrets, never commit
*.tfstate.*             # state backups
crash.log               # crash logs may contain sensitive data
*.tfvars                # often hold secrets/env values
*.tfvars.json
override.tf             # local overrides
override.tf.json
*_override.tf
*_override.tf.json
.terraformrc            # local CLI config
terraform.rc

# DO commit this — it locks provider versions/checksums for everyone:
!.terraform.lock.hcl
```

Rules:
- **Commit:** `*.tf`, `.terraform.lock.hcl`, `README.md`.
- **Ignore:** `.terraform/`, `*.tfstate*`, `*.tfvars` (unless you're 100% sure
  no secrets), crash logs.
- If a secret ever gets committed: rotate it immediately — git history keeps it
  forever otherwise.

---

## Cheat Sheet

```bash
terraform init            # set up project, download providers
terraform fmt -recursive  # format code
terraform validate        # check config
terraform plan            # preview changes
terraform apply           # apply changes (confirm yes)
terraform apply -auto-approve   # skip prompt (CI only, be careful)
terraform destroy         # tear down
terraform show            # show current state
terraform state list      # list resources
terraform output          # show outputs
terraform workspace list  # list workspaces
terraform providers       # show provider requirements
```

**The golden loop:** edit `.tf` → `fmt` → `validate` → `plan` (read it!) →
`apply`. Never skip reading the plan.

---

### Suggested order to actually do this

1. Phase 1 install → confirm `terraform version`.
2. Phase 2–3 local_file project → feel the init/plan/apply/destroy loop.
3. Phase 4 add variables/outputs.
4. Phase 5 open `terraform.tfstate` in an editor, see your data inside it.
5. Phase 7 Docker nginx → first "real" resource.
6. Phase 8 refactor into a module.
7. Phase 10 run fmt/validate/tflint/checkov on your code.
8. Phase 9 + 12 internalize security & git rules before touching any cloud.

Only after all that, attempt Phase 6 (cloud backend) with a real provider.
```
