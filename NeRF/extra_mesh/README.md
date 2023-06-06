## Extra a mesh from give model
In this `README.md` file, we will be going extra a mesh from the check points.

We provide two ways for see your trained model, one with command line, the other with jupyternotebook

### Install
You need to install 
```
pip install pymcubes trimesh    # for mesh
pip install plotly polyscope    # for visualization
```

### Command line
Please type `python extra_mesh.py -h` for descriptions of command line.

Gennerally, you need to coustomize these parameters
```
python extra_mesh.py \
--model ../pretrained/lego_18000.tar \
--save_path ./lego.ply \
--bound_min [-2,-2,-2] \
--bound_max [2,2,2] \
--visualize polyscope
```
The suggested parameters of provided pretrained models were provided in  [suggestions](#suggestions) 

And you can select your visualization tool either [Polyscope](https://polyscope.run/py/)(light weight, need `OpenGL` for backend, you can select and see the position of vertices) or [plotly](https://plotly.com/python/3d-mesh/) (in web browser, friendly for `jupyter`).


### Jupyter notebook
Install jupyter notebook (`pip install jupyter`) and type (`jupyter notebook`), find the [tutorial](./extra_mesh.ipynb) in your web browser (or directly open it with vscode). For details, please follow the jupyter notebook [tutorial](./extra_mesh.ipynb).
(`polyscope` is not well-integrated with `jupyter-notebook`, will cause bug unexpectedly.)

### Suggestions:
Generally, we provide pretrained model, and they were tested to be lied at bounds below
```
    ficus: bound_min [-0.5, -1, -1.5], bound_max [0.5, 1, 1.5]
    chair: bound_min [-1, -1, -1],     bound_max [1, 1, 1.5]
    lego:  bound_min [-2, -2, -0.5],   bound_max [2, 2, 2] 
    fern:  bound_min [-2, -2, -0.5],   bound_max [2, 2, 1] 
```
If you are handling with your own data, please tried for several times to the essential content (`polyscope` is friendly for positions).

### Special Thanks
The mesh extration code is borrowed from [NeuS](https://github.com/Totoro97/NeuS).