## Preprocessing your own data!
To preprocess your own data, you need colmap for extrinsic parameters estimation.

### Install colmap
To install colmap on Linux, you just need to 
```
sudo apt install colmap
```
where `apt` can be replaced with another package manager (e.g. `pacman` on `archlinux` (`pacman -Sy colmap`) ). To the same reason, you can install on `MaxOS` with `brew install colmap`

Note that the dependences of `colmap` were

```
sudo apt-get install \
    git \
    cmake \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev
sudo apt-get install libcgal-qt5-dev
```


To install on Windows, please download the `.exe` installer from the [official website](https://colmap.github.io/install.html) and set it into your `PATH`.

The, install `ffmpeg` for your computer with
```
Linux: sudo apt install libffmpeg-dev # (the same for other Linux platforms)
MacOS: brew install ffmpeg
```
For windows, please search `ffmpeg windows` for your computer and add it into your `PATH`.

### How to preprocess
1. Place your images/videos into `ANY_PLACE/[IMAGE_FOLDER]/` or `ANY_PLACE/[VIDEO_NAME]` 
2. For preprocess images, use 
 ```
 python colmap2nerf.py --images ANY_PLACE/[IMAGE_FOLDER] --run_colmap
 ```
 this will produce a `transform.json` file for extrinsic parameters and intrinsic parameters of cameras.

3. For preprocess video, use `python colmap2nerf.py --video_in ANY_PLACE/[VIDEO_NAME] --run_colmap`, this will produce a `transform.json` in this folder for extrinsic parameters and intrinsic parameters of camera, and produce a `ANY_PLACE/images/` folder for relative images.

Note that if any issue happened, it might be 
1. Your libraries are not fully installed (e.g. `freeimage` for `.png` only but you got `.jpg`, `qt` of `opencv_python` need reinstalled).
2. Your images are not sufficient engougth for a good estimation(seriously possible).
3. Your cpu memory is not enough for parallel computing of `colmap` (maybe your image is too huge, suggestion: use [resize.py](./resize.py) for smaller image (but this might cause less features), see code for details.

And also be patient that `colmap` might be slow and noisy(~5mins), but this is the only way...


### How to use the preprocessed data?
You can place the `./[IMAGES]/` data with `./transform.json` together as
```
    ./[CASE_NAME]/
    ├── images
    │   ├── 001.png
    │   ├── 002.png
    │   └── ...
    └── transform.json
```
When using nerf, set its type as `custom`.

### Warning:
Currently the type of `custom` is not avaliable for `train.py`, maybe a little of hacking is good.

### Special Thanks
This is mainly refered to [instant-ngp](https://github.com/NVlabs/instant-ngp)'s data preprocessing.