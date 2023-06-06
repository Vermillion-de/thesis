### Everything you want to play around in this project

## something you can set up by yourself.
TORCH_VERSION=1.12.0
CUDA_VERSION=116

## set up environments
setup_env: create_env, pip_env

create_env:
	conda create -n nerf -y python=3.8
	conda activate nerf
pip_env:
	pip install torch==${TORCH_VERSION}+cu${CUDA_VERSION} --extra-index-url https://download.pytorch.org/whl/cu${CUDA_VERSION}
	pip install configargparse numpy imageio opencv_python tqdm

## download datasets
download_data:
	mkdir -p data
	wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz
	wget http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/nerf_example_data.zip
	# mv tiny_nerf_data.npz ./data/
	mv nerf_example_data.zip ./data/
	unzip ./data/nerf_example_data.zip -d ./data/

## trainning demos, remind your gpu memory >= 8g
train_demo:	train_lego train_fern
train_lego:
	python train.py --config ./configs/lego.txt
train_fern:
	python train.py --config ./configs/fern.txt
train_blender:
	python train.py --config ./configs/materials.txt
	python train.py --config ./configs/mic.txt
	python train.py --config ./configs/ficus.txt
	python train.py --config ./configs/chair.txt

## extra and visualize a pretrained model
env_mesh:
	pip install trimesh pymcubes plotly polyscope 
extra_mesh_demo: env_mesh
	python ./extra_mesh/extra_mesh.py