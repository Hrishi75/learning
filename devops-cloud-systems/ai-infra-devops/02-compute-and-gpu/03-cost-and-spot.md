# GPU Cost Control and Spot Instances

GPUs are the biggest line item in AI infra. This is how you keep the bill sane.

## Where the Money Goes

- **Idle GPUs.** A GPU you booked but aren't using bills the same as a busy
  one. Idle = pure waste. This is the #1 cost leak.
- **Over-provisioned size.** Renting an 80GB GPU for a model that fits in 24GB.
- **24/7 dev/lab resources** nobody turned off.
- **Cross-AZ / egress data transfer** for big datasets and model artifacts.

Mental model: optimize **utilization first, price second**. A cheaper GPU at
10% utilization still wastes money.

## Levers, Highest Impact First

1. **Scale to zero when idle.** Spiky inference: scale GPU replicas (and node
   pool) to 0 when no traffic. Biggest single saving for non-24/7 workloads.
2. **Right-size the GPU.** Match VRAM to actual need + headroom (see
   `00-gpu-fundamentals.md`). Quantize so a smaller GPU fits.
3. **Batch requests.** Continuous batching (vLLM/TGI) raises throughput per
   GPU dramatically — same hardware serves far more.
4. **Share GPUs.** MIG / time-slicing so several small workloads share one card.
5. **Spot / preemptible** for interruptible work (see below).
6. **Schedule down dev/lab.** Auto-stop notebooks and dev clusters off-hours.

## Spot / Preemptible Instances

Cloud sells spare GPU capacity at a steep discount (often 60-90% off) with a
catch: the provider can **reclaim it with little warning** (e.g. ~2 min).

Good fit:
- Training with checkpointing (resume after interruption).
- Batch / offline inference.
- Stateless inference behind a queue, with on-demand fallback.

Bad fit:
- Single-replica low-latency production serving with no fallback.
- Long jobs with no checkpointing (you lose everything on reclaim).

### Surviving interruptions

- **Checkpoint often** to durable storage; resume from last checkpoint.
- **Handle the termination signal** to drain/save before eviction.
- **Mix capacity:** spot for bulk + a small on-demand baseline for SLAs.
- **Spread across instance types / AZs** so one capacity crunch doesn't kill
  all replicas at once.

## Guardrails (set these on day one)

- **Budgets + alerts** per project/team (cloud billing budgets).
- **Cost dashboards** by GPU type and namespace/label.
- **Tag/label everything** (team, project, env) so spend is attributable.
- **Idle detector:** alert/auto-stop GPUs under X% utilization for N minutes.
- **TTL on lab resources:** auto-expire experiment clusters.
- **Quotas:** cap how many GPUs a team can request.

## Quick Utilization Check

```bash
# live utilization + memory on a node
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv -l 5
```

If `utilization.gpu` sits near 0 while the GPU is allocated, you are paying for
nothing — batch more, share the GPU, or scale down.

## Build vs Buy (managed)

- **Self-managed GPU on K8s:** cheapest per-hour, most ops work (drivers,
  scaling, reliability on you).
- **Managed inference / serverless GPU:** higher per-hour, near-zero ops, often
  scale-to-zero built in. Cheaper overall for spiky/low-volume because you stop
  paying for idle.

Rule: low/spiky volume -> managed or serverless. High steady volume -> self-
managed reserved/committed capacity wins.

## References

- AWS GPU spot best practices: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html
- GCP preemptible/Spot VMs: https://cloud.google.com/compute/docs/instances/spot
