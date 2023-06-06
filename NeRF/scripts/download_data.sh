#! /bin/bash
export GIT_ROOT=$(git rev-parse --show-toplevel)

mkdir -p ${GIT_ROOT}/data
# wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz
# wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/nerf_example_data.zip

# mv tiny_nerf_data.npz  nerf_example_data.zip  ${GIT_ROOT}/data/

unzip ${GIT_ROOT}/data/nerf_example_data.zip -d ${GIT_ROOT}/data/