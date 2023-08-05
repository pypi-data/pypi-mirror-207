import torch
import torch.autograd
from torch.autograd import Function
from torch.autograd.function import once_differentiable
import sparse_filter_convolution.sparse_unfold_cuda_ext as sparse_unfold_cuda_ext

class SparseUnfoldFunction(Function):
    @staticmethod
    def forward(ctx, padded_signal, top_k_indices, n):
        if padded_signal.is_cuda:
            sparse_unfolded_signal = torch.zeros(padded_signal.shape[0], padded_signal.shape[1], n, top_k_indices.shape[1], device=padded_signal.device)
            sparse_unfold_cuda_ext.sparse_unfold(padded_signal, top_k_indices, sparse_unfolded_signal, n)
        else:
            sparse_unfolded_signal = torch.zeros(padded_signal.shape[0], padded_signal.shape[1], n, top_k_indices.shape[1])
            sparse_unfold_cuda_ext.sparse_unfold_cpu(padded_signal, top_k_indices, sparse_unfolded_signal, n)
        return sparse_unfolded_signal

    @staticmethod
    @once_differentiable
    def backward(ctx, grad_output):
        raise NotImplementedError("Backward pass is not implemented for SparseUnfoldFunction.")

sparse_unfold = SparseUnfoldFunction.apply
