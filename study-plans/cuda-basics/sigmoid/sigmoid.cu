#include <cuda_runtime.h>
#include <math.h>

__global__ void sigmoid_kernel(const float* input, float* output, int N) {
    // Store N element-wise results in output; this kernel returns no value.
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i<N){
        float x = input[i];
        output[i] = 1/(1.0f + expf(-x));
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    sigmoid_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}