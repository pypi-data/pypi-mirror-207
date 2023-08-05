import torch
import torch.autograd
from torch.autograd import Function
from torch.autograd.function import once_differentiable
import sparse_filter_convolution.sparse_unfold_cuda_ext as sparse_unfold_cuda_ext

class SparseUnfoldFunction(Function):
    @staticmethod
    def forward(ctx, signal, top_k_indices, filter_length):
        if signal.is_cuda:
            sparse_unfolded_signal = torch.zeros(signal.shape[0], signal.shape[1], filter_length, top_k_indices.shape[1], device=signal.device)
            sparse_unfold_cuda_ext.sparse_unfold(signal, top_k_indices, sparse_unfolded_signal, filter_length)
        else:
            sparse_unfolded_signal = torch.zeros(signal.shape[0], signal.shape[1], filter_length, top_k_indices.shape[1])
            sparse_unfold_cuda_ext.sparse_unfold_cpu(signal, top_k_indices, sparse_unfolded_signal, filter_length)

        ctx.save_for_backward(top_k_indices, signal)
        ctx.filter_length = filter_length
        return sparse_unfolded_signal

    @staticmethod
    def backward(ctx, grad_output):
        top_k_indices, signal = ctx.saved_tensors
        filter_length = ctx.filter_length

        if grad_output.is_cuda:
            grad_signal = torch.zeros_like(signal)
            sparse_unfold_cuda_ext.sparse_unfold_backward(grad_output, top_k_indices, grad_signal, filter_length)
        else:
            grad_signal = torch.zeros_like(signal)
            sparse_unfold_cuda_ext.sparse_unfold_backward_cpu(grad_output, top_k_indices, grad_signal, filter_length)

        return grad_signal, None, None

sparse_unfold = SparseUnfoldFunction.apply
