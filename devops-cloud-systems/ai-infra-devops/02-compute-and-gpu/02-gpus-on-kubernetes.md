# GPUs on Kubernetes

How a Kubernetes cluster knows about GPUs and how a pod gets one.

## How K8s Sees GPUs

Kubernetes does not understand GPUs natively. A **device plugin** advertises
them as a schedulable resource named `nvidia.com/gpu`. You then request that
resource like CPU or memory.

The clean way to install everything (driver, toolkit, device plugin, metrics)
is the **NVIDIA GPU Operator** — it manages the whole GPU stack on nodes so you
don't hand-configure each node.

```bash
# is any node advertising GPUs?
kubectl get nodes -o custom-columns=NAME:.metadata.name,GPU:.status.allocatable.'nvidia\.com/gpu'

# detail on one node
kubectl describe node <node> | grep -i nvidia.com/gpu
```

If allocatable GPU is `<none>` or 0, the device plugin / operator is not
working — fix that before deploying workloads.

## Requesting a GPU in a Pod

GPUs are **non-divisible by default**: you request whole GPUs as integers, and
limit must equal request (no overcommit).

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-test
spec:
  restartPolicy: Never
  containers:
    - name: cuda
      image: nvidia/cuda:12.4.1-base-ubuntu22.04
      command: ["nvidia-smi"]
      resources:
        limits:
          nvidia.com/gpu: 1     # whole GPU; request==limit implied
```

```bash
kubectl apply -f gpu-test.yaml
kubectl logs gpu-test            # should print the nvidia-smi table
```

A deployment that serves a model looks the same, just with your image and a
`Deployment` spec requesting `nvidia.com/gpu: 1`.

## Getting Pods Onto GPU Nodes

In mixed clusters (CPU + GPU nodes), keep non-GPU work off expensive GPU nodes.

- **nodeSelector / affinity:** target GPU node labels (the operator labels
  nodes with GPU product, e.g. `nvidia.com/gpu.product`).
- **Taints + tolerations:** taint GPU nodes so only GPU pods (with the matching
  toleration) land there.

```yaml
spec:
  tolerations:
    - key: "nvidia.com/gpu"
      operator: "Exists"
      effect: "NoSchedule"
  nodeSelector:
    nvidia.com/gpu.present: "true"
```

## Sharing One GPU Across Pods

Whole-GPU-per-pod wastes money for small models. Two ways to share:

| Method | What it does | Isolation | Use when |
|--------|--------------|-----------|----------|
| **MIG** | Hardware-splits one big GPU (e.g. A100/H100) into fixed slices | Strong (memory + compute isolated) | Multi-tenant, predictable QoS |
| **Time-slicing** | Multiple pods take turns on one GPU | Weak (shared memory, no fault isolation) | Dev/test, bursty light loads |

Both are configured via the GPU Operator. MIG = production multi-tenant.
Time-slicing = cheap dev sharing, not for noisy/critical neighbors.

## Autoscaling GPU Nodes

- **Cluster Autoscaler / Karpenter:** add GPU nodes when GPU pods are
  `Pending`, remove when idle. GPU nodes are pricey — scale down aggressively.
- Scale-to-zero GPU node pools save the most money for spiky inference.
- Pair with **HPA / KEDA** to scale pod replicas on a metric (queue depth,
  GPU util, requests/sec) — see `05-model-serving-inference/`.

## Gotchas

- Pod stuck `Pending` with "Insufficient nvidia.com/gpu" = no free GPU; need a
  node to scale up or a smaller request (MIG slice).
- Forgetting tolerations = GPU pod never schedules onto a tainted GPU node.
- Requesting GPUs for a CPU-only job = wasted, expensive idle GPU.
- No resource limits on CPU/mem of GPU pods = noisy neighbor can starve the
  node even though the GPU is fine.

## References

- GPU Operator: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html
- K8s schedule GPUs: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
- MIG user guide: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/
