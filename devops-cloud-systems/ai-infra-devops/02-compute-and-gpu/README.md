# 02 - Compute and GPU

The hardware layer of AI infra: what GPUs do, the software stack to drive them,
how Kubernetes schedules them, and how to keep the bill under control.

## Read In Order

| File | Topic |
|------|-------|
| [00-gpu-fundamentals.md](00-gpu-fundamentals.md) | CPU vs GPU, VRAM/bandwidth/FLOPS, VRAM estimation, precision, multi-GPU |
| [01-cuda-drivers-stack.md](01-cuda-drivers-stack.md) | Driver vs CUDA runtime, compatibility, GPUs in Docker, failure map |
| [02-gpus-on-kubernetes.md](02-gpus-on-kubernetes.md) | Device plugin / GPU Operator, requesting GPUs, MIG, time-slicing, autoscaling |
| [03-cost-and-spot.md](03-cost-and-spot.md) | Utilization-first cost control, spot/preemptible, budgets and guardrails |

## One-Line Takeaways

- VRAM is the limit you hit first — size for weights + headroom.
- Host has the **driver**; the image has the **CUDA runtime**. Keep them compatible.
- K8s needs a device plugin to see `nvidia.com/gpu`; request whole GPUs (or MIG slices).
- Idle GPUs are the biggest cost leak — optimize utilization before chasing cheaper price.
