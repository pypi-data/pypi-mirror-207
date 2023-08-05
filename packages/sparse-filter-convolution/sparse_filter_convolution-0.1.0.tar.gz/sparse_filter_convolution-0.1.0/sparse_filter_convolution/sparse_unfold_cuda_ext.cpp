#include <torch/extension.h>

__global__ void sparse_unfold_kernel(const float* padded_signal, const int* top_k_indices,
                                     float* sparse_unfolded_signal, int b, int d, int n, int k) {
    int bi = blockIdx.x * blockDim.x + threadIdx.x;
    int di = blockIdx.y * blockDim.y + threadIdx.y;
    int ni = blockIdx.z * blockDim.z + threadIdx.z;

    if (bi < b && di < d && ni < n) {
        int idx = di * k;
        for (int ki = 0; ki < k; ++ki) {
            int signal_idx = bi * d * n + di * n + ni + top_k_indices[idx + ki];
            int sparse_idx = bi * d * n * k + di * n * k + ni * k + ki;
            sparse_unfolded_signal[sparse_idx] = padded_signal[signal_idx];
        }
    }
}

void sparse_unfold_cuda(const at::Tensor& padded_signal, const at::Tensor& top_k_indices,
                        at::Tensor& sparse_unfolded_signal, int n) {
    int b = padded_signal.size(0);
    int d = padded_signal.size(1);
    int k = top_k_indices.size(1);

    dim3 blockDim(16, 16, 8); // Change these values based on your GPU capabilities
    dim3 gridDim((b + blockDim.x - 1) / blockDim.x,
                 (d + blockDim.y - 1) / blockDim.y,
                 (n + blockDim.z - 1) / blockDim.z);

    sparse_unfold_kernel<<<gridDim, blockDim>>>(padded_signal.data_ptr<float>(), top_k_indices.data_ptr<int>(),
                                                sparse_unfolded_signal.data_ptr<float>(), b, d, n, k);
    cudaDeviceSynchronize();
}

void sparse_unfold_cpu(const at::Tensor& padded_signal, const at::Tensor& top_k_indices,
                       at::Tensor& sparse_unfolded_signal, int n) {
    int b = padded_signal.size(0);
    int d = padded_signal.size(1);
    int k = top_k_indices.size(1);

    auto padded_signal_a = padded_signal.accessor<float, 3>();
    auto top_k_indices_a = top_k_indices.accessor<int, 2>();
    auto sparse_unfolded_signal_a = sparse_unfolded_signal.accessor<float, 4>();

    for (int bi = 0; bi < b; ++bi) {
        for (int di = 0; di < d; ++di) {
            for (int ni = 0; ni < n; ++ni) {
                for (int ki = 0; ki < k; ++ki) {
                    int signal_idx = ni + top_k_indices_a[di][ki];
                    sparse_unfolded_signal_a[bi][di][ni][ki] = padded_signal_a[bi][di][signal_idx];
                }
            }
        }
    }
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("sparse_unfold", &sparse_unfold_cuda, "Sparse Unfold (CUDA)");
    m.def("sparse_unfold_cpu", &sparse_unfold_cpu, "Sparse Unfold (CPU)");
}
