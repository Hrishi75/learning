# AI Infra / DevOps Roadmap

From "can deploy a model" to "can run an AI platform". Read top to bottom.

## Stage 1 - Foundations

- What an AI platform is: data -> train -> registry -> serve -> monitor.
- MLOps vs LLMOps: training-centric vs prompt/inference-centric ops.
- Lifecycle: experiment -> package -> deploy -> observe -> retrain.
- Where DevOps skills transfer: containers, CI/CD, IaC, observability.

## Stage 2 - Compute and GPU

- GPU basics: VRAM, FLOPS, why memory limits model size.
- CUDA, drivers, cuDNN, container toolkit.
- Scheduling GPUs on Kubernetes; MIG, time-slicing.
- Cost: on-demand vs spot/preemptible, scale-to-zero.

```bash
nvidia-smi
nvidia-smi --query-gpu=memory.used,memory.total --format=csv
```

## Stage 3 - Containers and Orchestration

- Build slim ML images (CUDA base, multi-stage, pinned deps).
- Kubernetes: pods, deployments, requests/limits, GPU resource requests.
- GPU Operator, device plugin.
- Distributed: Ray, Kubeflow, training operators.

```bash
kubectl get nodes -o wide
kubectl describe node <node> | grep -i nvidia.com/gpu
```

## Stage 4 - Data and Pipelines

- Data/feature pipelines, versioning (DVC, lakeFS).
- Training pipelines: reproducible, parameterized, tracked.
- Experiment tracking + model registry (MLflow).
- CI/CD for ML: test data + model + code, gated promotion.

## Stage 5 - Model Serving and Inference

- Serving patterns: online, batch, streaming.
- LLM serving: vLLM, TGI, Triton; continuous/dynamic batching, KV cache.
- KServe / model mesh, autoscaling, canary rollout.
- Latency vs throughput vs cost tradeoffs; quantization.

## Stage 6 - LLMOps

- Prompt + config versioning, eval harness, regression gates.
- RAG infra: chunking, embeddings, vector DB (pgvector, Qdrant, etc.).
- Guardrails, rate limiting, caching, fallback/routing.
- Feedback capture and offline eval loops.

## Stage 7 - Observability and Cost

- Model monitoring: drift, quality, hallucination/eval signals.
- System metrics: GPU util, latency, queue depth (Prometheus/Grafana).
- Tracing for LLM apps (token usage, spans).
- Cost dashboards, budgets, idle-resource alerts.

## Stage 8 - Infrastructure as Code

- Terraform for GPU node pools and managed AI services.
- GitOps (Argo CD / Flux) for cluster + model deploys.
- Secrets, networking, multi-environment structure.

## Practice Order

1. Containerize a model, run locally.
2. Serve an LLM with vLLM behind an API.
3. Deploy to Kubernetes with a GPU request.
4. Add MLflow tracking + registry.
5. Build a RAG service with a vector DB.
6. Add Prometheus/Grafana + cost alerts.
7. Terraform a GPU node pool + GitOps deploy.
