import torch

print("Torch version:", torch.__version__)
print("GPU Detected:", torch.cuda.device_count())
print("CUDA Version:", torch.version.cuda)
print("NCCL Version:", torch.cuda.nccl.version())
