# CUDA, Drivers, and the GPU Software Stack

The layers that sit between your code and the GPU. Most "GPU not found" pain
comes from a mismatch in this stack.

## The Stack (bottom to top)

```
Hardware:        NVIDIA GPU
NVIDIA driver:   kernel module, talks to the card        (host)
CUDA toolkit:    nvcc compiler + CUDA runtime libraries
cuDNN / libs:    tuned deep-learning kernels
Framework:       PyTorch / TensorFlow / JAX (ships its own CUDA build)
Your code:       model + training/serving logic
```

Key idea: the **driver lives on the host**. The **CUDA runtime ships inside
your container / framework**. They must be compatible.

## The Compatibility Rule

- Driver version must be **>=** the CUDA runtime version it supports.
  Newer driver runs older CUDA fine. Old driver + new CUDA = fails.
- You usually do NOT install the full CUDA toolkit yourself. PyTorch wheels
  bundle their own CUDA runtime. You only need a recent enough **driver**.
- Check what the host has:

```bash
nvidia-smi            # shows driver version + max CUDA version supported
nvcc --version        # shows installed CUDA toolkit (often absent, that's ok)
```

`nvidia-smi` "CUDA Version" = highest CUDA the *driver* supports, NOT what is
installed. People misread this constantly.

## Verify GPU is Actually Usable

```bash
# host: is the card visible?
nvidia-smi

# python: does the framework see it?
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

If `nvidia-smi` works but PyTorch says `False`:
- CPU-only PyTorch wheel installed (reinstall the CUDA build).
- Container can't see the GPU (missing `--gpus all` / runtime).
- Driver too old for that PyTorch's bundled CUDA.

## GPUs Inside Docker

You need the **NVIDIA Container Toolkit** on the host. It lets containers reach
the host driver. CUDA itself goes in the image.

```bash
# run a container with GPU access
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

If that prints the GPU table, Docker GPU access works. If not, fix the host
toolkit before touching your app.

Dockerfile pattern for ML:

```dockerfile
# pick a CUDA base that matches your framework's needs
FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
# install the CUDA build of torch (index url picks the cuda variant)
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cu124
COPY . /app
WORKDIR /app
```

Use `*-runtime` images for serving (smaller), `*-devel` only if you must
compile CUDA code (`nvcc`).

## Common Failure Map

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `nvidia-smi` not found on host | driver not installed | install NVIDIA driver |
| `torch.cuda.is_available()` False | CPU wheel / old driver / no `--gpus` | reinstall cuda torch; check driver; pass `--gpus all` |
| `docker run --gpus all` errors | container toolkit missing | install NVIDIA Container Toolkit |
| `CUDA out of memory` | model+batch too big | smaller batch, quantize, bigger GPU, multi-GPU |
| version mismatch errors | driver < CUDA runtime | upgrade host driver |

## What To Install Where (summary)

- **Host:** NVIDIA driver + NVIDIA Container Toolkit. That's it for serving.
- **Image:** CUDA runtime (via base image) + framework CUDA build.
- **Avoid:** hand-installing full CUDA toolkit on the host unless you compile
  kernels. It just creates version drift.

## References

- NVIDIA Container Toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
- PyTorch install selector: https://pytorch.org/get-started/locally/
- CUDA compatibility: https://docs.nvidia.com/deploy/cuda-compatibility/
