# AI Infra / DevOps for AI Engineering

How to build, ship, scale, and operate ML and LLM systems in production.
This is the DevOps/platform side of AI: GPUs, containers, serving, pipelines,
LLMOps, observability, cost, and Infrastructure as Code.

> Cost rule: GPU compute is expensive. Use spot/preemptible where safe, set
> budgets and alerts, scale to zero when idle, and tear down lab clusters.

## How To Use This Folder

1. Read `01-foundations/` for the MLOps vs LLMOps landscape and the roadmap.
2. Learn the hardware in `02-compute-and-gpu/`.
3. Package and orchestrate workloads in `03-containers-orchestration/`.
4. Build data + training pipelines in `04-data-and-pipelines/`.
5. Serve models in `05-model-serving-inference/`.
6. Operate LLM apps in `06-llmops/`.
7. Monitor and control spend in `07-observability-and-cost/`.
8. Codify infra in `08-iac-for-ai/`.
9. Build labs in `09-projects/`.
10. Prep with `10-interview-questions/`.

## Folder Map

| Folder | Purpose |
|--------|---------|
| `01-foundations/` | MLOps vs LLMOps, AI platform landscape, roadmap |
| `02-compute-and-gpu/` | GPUs/accelerators, CUDA, drivers, scheduling, spot |
| `03-containers-orchestration/` | Docker for ML, Kubernetes, Kubeflow, Ray, GPU operator |
| `04-data-and-pipelines/` | Data/feature pipelines, training pipelines, CI/CD for ML, MLflow |
| `05-model-serving-inference/` | vLLM, Triton, TGI, KServe, batching, autoscaling |
| `06-llmops/` | Prompt/version mgmt, RAG infra, vector DBs, eval, guardrails |
| `07-observability-and-cost/` | Drift/quality monitoring, GPU metrics, tracing, cost control |
| `08-iac-for-ai/` | Terraform for GPU clusters, managed AI services, GitOps |
| `09-projects/` | Hands-on labs, beginner to advanced |
| `10-interview-questions/` | AI infra / MLOps / LLMOps interview Q&A |
| `cheatsheets/` | kubectl, nvidia-smi, vLLM, MLflow quick recall |

## Core Tooling Reference

- Kubernetes: https://kubernetes.io/docs/home/
- NVIDIA GPU Operator: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html
- vLLM: https://docs.vllm.ai/en/latest/
- NVIDIA Triton: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html
- KServe: https://kserve.github.io/website/latest/
- Ray: https://docs.ray.io/en/latest/
- MLflow: https://mlflow.org/docs/latest/index.html
- Kubeflow: https://www.kubeflow.org/docs/
