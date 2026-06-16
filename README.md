# OpenCV Learning Path

A structured, notebook-based path for learning OpenCV with Python, running inside a containerized Jupyter Lab environment.

## Setup

### 1. Prerequisites

- Docker Desktop installed and running

### 2. Build and start the container

```powershell
docker compose up --build
```

This builds the image from `Dockerfile` (Python + OpenCV + Jupyter Lab) and starts Jupyter Lab on port `8888`. The project folder is mounted into the container, so any changes made on the host are immediately reflected inside.

### 3. Open Jupyter Lab

Open `http://localhost:8888` in your browser. No token is required.

To run notebooks from VS Code instead, connect the Jupyter extension to `http://localhost:8888` via **"Select Another Kernel" → "Existing Jupyter Server"**.

## Models folder (Topic 19 — OpenCV DNN)

The `models/` folder is not tracked in git (model files are large binaries). To run the DNN notebook (`15_dnn.ipynb`), create the folder and download the required files:

```powershell
New-Item -ItemType Directory -Force models
Invoke-WebRequest -Uri "https://github.com/onnx/models/raw/main/validated/vision/classification/mobilenet/model/mobilenetv2-12.onnx" -OutFile "models/mobilenetv2.onnx"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt" -OutFile "models/imagenet_classes.txt"
Invoke-WebRequest -Uri "https://github.com/onnx/models/raw/main/validated/vision/object_detection_segmentation/yolov4/model/yolov4.onnx" -OutFile "models/yolov4.onnx"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt" -OutFile "models/deploy.prototxt"
Invoke-WebRequest -Uri "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel" -OutFile "models/res10_300x300_ssd_iter_140000.caffemodel"
```

- `mobilenetv2.onnx` + `imagenet_classes.txt` — image classification example
- `yolov4.onnx` (~251 MB) — object detection example (boxes + NMS)
- `deploy.prototxt` + `res10_300x300_ssd_iter_140000.caffemodel` (~10 MB) — face detection with OpenCV's ResNet-SSD Caffe model

## Other ignored folders

- `images/` — input images used by the notebooks (add your own test images here)
- `outputs/` — generated outputs from running the notebooks

These folders are not tracked in git but are available inside the container via the volume mount.
