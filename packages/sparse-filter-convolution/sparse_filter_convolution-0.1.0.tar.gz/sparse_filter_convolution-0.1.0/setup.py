from setuptools import setup, Extension
from torch.utils import cpp_extension

with open("README.md", "r", encoding="utf-8") as fh:
      long_description = fh.read()

setup(
      name='sparse_filter_convolution',
      version='0.1.0',
      author='Your Name',
      author_email='tobias.katsch42@gmail.com',
      description='A CUDA extension for PyTorch to perform sparse filter convolution',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/tobiaskatsch/sparse_filter_convolution.git',
      ext_modules=[
            cpp_extension.CUDAExtension(
                  'sparse_filter_convolution.sparse_unfold_cuda_ext',
                  ['sparse_filter_convolution/sparse_unfold_cuda_ext.cpp']
            )
      ],
      cmdclass={'build_ext': cpp_extension.BuildExtension},
      packages=['sparse_filter_convolution'],
      install_requires=['torch']
)
