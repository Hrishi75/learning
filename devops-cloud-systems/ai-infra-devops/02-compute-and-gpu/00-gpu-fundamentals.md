# GPU Fundamentals for AI Infra

Why AI runs on GPUs and what numbers actually matter when you size hardware.

## CPU vs GPU

- CPU: few powerful cores, great at sequential logic and branching.
- GPU: thousands of small cores, great at doing the *same* math on lots of
  data at once (matrix multiply). Neural nets are mostly matrix multiply, so
  GPUs win.
- Rule of thumb: training and large-model inference = GPU; light/classical ML
  and glue code = CPU is fine.

## The Numbers That Matter

| Spec | What it means | Why you care |
|------|---------------|--------------|
| VRAM (GB) | Memory *on* the GPU | Hard limit on model size + batch + KV cache. Out of VRAM = crash. |
| Memory bandwidth (GB/s) | How fast it feeds the cores | LLM inference is usually bandwidth-bound, not compute-bound. |
| FLOPS (TFLOPs) | Raw math throughput | Matters for training and big batches. |
| Precision support | FP32/FP16/BF16/FP8/INT8 | Lower precision = less VRAM + faster, small accuracy cost. |
| Interconnect | NVLink / PCIe | Speed between GPUs for multi-GPU training. |

**VRAM is the spec you hit first.** Most "it won't run" problems are out-of-memory, not "too slow".

## Estimating Model VRAM

Weights only, rough formula:

```
VRAM_weights (GB) ~= params (billions) * bytes_per_param
```

bytes_per_param by precision:
- FP32 = 4
- FP16 / BF16 = 2
- INT8 = 1
- INT4 = 0.5

Examples (weights alone):
- 7B in FP16 ~= 14 GB
- 7B in INT4 ~= 3.5 GB
- 70B in FP16 ~= 140 GB (needs multiple GPUs)

Then add overhead:
- **Inference:** + KV cache (grows with context length * batch) + activations.
  Plan ~1.2x-2x of weights for headroom.
- **Training:** weights + gradients + optimizer state (Adam ~2x weights) +
  activations. Plan ~4x-6x of weights, or use sharding/offload.

## Precision Cheat Notes

- **FP32:** baseline, accurate, heavy. Rarely needed end-to-end now.
- **BF16:** same exponent range as FP32, half the bits. Default for modern
  training. Stable.
- **FP16:** half precision, smaller range, can overflow; needs loss scaling.
- **FP8 / INT8 / INT4:** quantization. Big VRAM + speed wins for inference.
  Slight quality drop; validate with eval, do not assume.

## Multi-GPU: When and How

You go multi-GPU when the model or batch does not fit, or you need more
throughput.

- **Data parallel:** copy model on each GPU, split the batch. Simple, needs
  model to fit on one GPU.
- **Tensor parallel:** split a single layer's matrices across GPUs. For models
  too big for one GPU. Needs fast interconnect (NVLink).
- **Pipeline parallel:** put different layers on different GPUs.
- **FSDP / ZeRO:** shard weights+gradients+optimizer state across GPUs to fit
  huge models. Standard for large training.

Interconnect matters: NVLink (fast, intra-node) >> PCIe >> Ethernet between
nodes. Cross-node training needs fast networking (InfiniBand / RoCE) or comms
become the bottleneck.

## Picking a GPU (mental model)

1. Compute model VRAM need (weights + headroom).
2. Pick smallest GPU/precision that fits with margin.
3. If it does not fit one GPU: quantize, or go multi-GPU (tensor/FSDP).
4. For inference throughput: more memory bandwidth + batching beats raw FLOPS.

## Key Terms

- **CUDA core / SM:** the GPU's compute units.
- **Tensor core:** specialized unit for fast low-precision matrix multiply.
- **KV cache:** stored attention keys/values during generation; grows with
  context length, eats VRAM fast at long contexts.
- **MIG (Multi-Instance GPU):** slice one big GPU into isolated smaller GPUs.
- **OOM:** out of memory — the #1 failure you will hit.
