#! /bin/bash
export GIT_ROOT=$(git rev-parse --show-toplevel)

pip install gdown

## nerf_synthetic.zip
gdown https://drive.google.com/uc?id=18JxhpWD-4ZmuFKLzKlAw-w5PpzZxXOcG
mv nerf_synthetic.zip ${GIT_ROOT}/data/
unzip ${GIT_ROOT}/data/nerf_synthetic.zip -d ${GIT_ROOT}/data/

## nerf_real_360.zip
gdown https://drive.google.com/uc?id=1jzggQ7IPaJJTKx9yLASWHrX8dXHnG5eB
mv nerf_real_360.zip ${GIT_ROOT}/data/
unzip ${GIT_ROOT}/data/nerf_real_360.zip -d ${GIT_ROOT}/data/

## nerf_llff_data.zip
gdown https://drive.google.com/uc?id=16VnMcF1KJYxN9QId6TClMsZRahHNMW5g
mv nerf_llff_data.zip ${GIT_ROOT}/data/
unzip ${GIT_ROOT}/data/nerf_llff_data.zip -d ${GIT_ROOT}/data/

## nerf_example_data.zip
gdown https://drive.google.com/uc?id=1xzockqgkO-H3RCGfkZvIZNjOnk3l7AcT
mv nerf_example_data.zip ${GIT_ROOT}/data/
unzip ${GIT_ROOT}/data/nerf_example_data.zip -d ${GIT_ROOT}/data/

## blend_files.zip
gdown https://drive.google.com/uc?id=1RjwxZCUoPlUgEWIUiuCmMmG0AhuV8A2Q
mv blend_files.zip ${GIT_ROOT}/data/
unzip ${GIT_ROOT}/data/blend_files.zip -d ${GIT_ROOT}/data/