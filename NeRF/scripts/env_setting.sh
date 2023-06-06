#! /bin/bash
export TORCH_VERSION=1.12.0 CUDA_VERSION=116
pip install trimesh pymcubes plotly polyscope
pip install torch==${TORCH_VERSION}+cu${CUDA_VERSION} --extra-index-url https://download.pytorch.org/whl/cu${CUDA_VERSION}
pip install configargparse numpy imageio opencv_python tqdm