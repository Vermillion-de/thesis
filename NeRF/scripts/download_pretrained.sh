#! /bin/bash
export GIT_ROOT=$(git rev-parse --show-toplevel)

wget https://github.com/bon-qi/nerf/releases/download/1.0/chair_020000.tar
wget https://github.com/bon-qi/nerf/releases/download/1.0/fern_020000.tar
wget https://github.com/bon-qi/nerf/releases/download/1.0/ficus_020000.tar
wget https://github.com/bon-qi/nerf/releases/download/1.0/lego_020000.tar
mv chair_020000.tar fern_020000.tar ficus_020000.tar lego_020000.tar ${GIT_ROOT}/pretrained