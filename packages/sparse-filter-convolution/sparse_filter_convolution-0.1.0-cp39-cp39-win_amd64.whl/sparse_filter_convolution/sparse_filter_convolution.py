import torch
from .sparse_unfold_cuda import sparse_unfold

def sparse_filter_convolution(signal, filter, k):

    if signal.shape[-1] != filter.shape[-1]:
        raise NotImplementedError("Only global convolutions are implemented")

    # signal: (batch_size, dim, seq_len)
    # filter: (dim, seq_len)

    filter = torch.flip(filter, dims=[1])

    b, d, n = signal.shape

    # Find the indices of the top_k elements in the filter
    _, top_k_indices = torch.topk(torch.abs(filter), k=k, dim=1) # (d, k)
    top_k_values = torch.gather(filter, 1, top_k_indices)

    padding = n - 1

    # Pad the signal with zero padding at the beginning
    padded_signal = F.pad(signal, (padding, 0, 0, 0, 0, 0), value=0)

    sparse_unfolded_signal = sparse_unfold(padded_signal, top_k_indices, n)

    output = torch.matmul(sparse_unfolded_signal, top_k_values.unsqueeze(0).unsqueeze(-1))  # (b, d, n, 1)
    output = output.squeeze(-1)  # (b, d, n)

    return output