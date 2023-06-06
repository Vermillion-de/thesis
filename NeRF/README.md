# nerf: a reimplementation
A Customized NeRF pipeline by Qi

## Install
To install the environment, you just need to type (assume `anaconda` or `miniconda` installed),
```
make setup_env
```
Or using scripts, after using `conda` (`conda create -n nerf -y python=3.8`, `conda activate nerf`) or it will on your default `python` environment.
```
bash ./scripts/env_setting.sh
```

Or using [requirements.txt](./requirements.txt), `python -m pip install -r ./requirements.txt`.

## Download dataset
To get a minimal dataset for traning demo, you just need to type
```
make download_data
```
Or using scripts,
```
bash ./scripts/download_data.sh
```
To get more dataset, see [`data/README.md`](./data/README.md) for details.

## Customized dataset
Please refer to [preprocess_data/README.md](./preprocess_data/README) for more information to a customized dataset (currently it was not fully supported).


## Trainning
To train a lego for yourself after the environment had been set up, you just need to type
```
make train_lego
```
Or using scripts,
```
bash ./scripts/train_lego.sh
```
This will make a `log` directory for check points, visualizations, etc.
See [makefile](./makefile) for other commands, and see [arg_parser.py](./arg_parser.py) for more options on trainning.

## Download pretrained
You can download pretrained model from our [release](https://github.com/bon-qi/nerf/releases/tag/1.0) page, and place then in [./pretrained](./pretrained/) fold.

## Extra your mesh
To extra a mesh yourself, you just need to type
```
make extra_mesh_demo
```
Or in extra_mesh.sh
```
bash ./srcipts/extra_mesh.sh
```
To be more customized, see [`extra_mesh/README.md`](./extra_mesh/README.md) for details.

Please see [makefile](./makefile) for more information.

## Reference
- [NeRF](https://www.matthewtancik.com/nerf) : original project page
- [D-NeRF](https://github.com/albertpumarola/D-NeRF): D-NeRF is based on the same project as this one.
- [NeuS](https://github.com/Totoro97/NeuS)
