# Face Blurring
**Face detection + Face blurring**
+ Detect all the faces in the input video
+ Blur all the detected faces and save them 

**Code Author: Shih-Yao (Mike) Lin**

## Dependencies
+ OpenCV >= 3.2.0.8
+ Tensorflow >= 1.4.1
+ MTCNN 

## Installation

* Clone this repo

```bash
git clone https://github.com/mikeshihyaolin/face_blurring.git
```
The directory tree should look like this:
```
${ROOT}
├── README.md
├── face_blurring.py
├── figs
│   ├── .DS_Store
│   ├── .blur1.png.icloud
│   ├── blur2.jpg
│   └── blur3.jpg
└── mtcnn
    ├── .DS_Store
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── layer_factory.cpython-36.pyc
    │   ├── mtcnn.cpython-36.pyc
    │   └── network.cpython-36.pyc
    ├── data
    │   └── .mtcnn_weights.npy.icloud
    ├── exceptions
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-36.pyc
    ├── layer_factory.py
    ├── mtcnn.py
    └── network.py
```

* Install dependencies
```
pip3 install -r ./requirements.txt
```

## Quick Start
```
python face_blurring.py --source_video [input video] --output_blur_img_folder [output folder]
```
For example,
```
python face_blurring.py --source_video ./example/video.mp4 --output_video ./blur
```

## Visualization results
![](figs/blur1.png)
![](figs/blur2.jpg)
![](figs/blur3.jpg)

The face detection process is heavily borrowed from a MTCNN implementation ([Link](https://github.com/ipazc/mtcnn.git))
