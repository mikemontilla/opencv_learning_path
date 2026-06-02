# OpenCV Learning Path

## Project goal

Learn OpenCV through Python scripts, progressing from fundamentals to GPU-accelerated video processing on Jetson hardware. Each concept is learned through small, focused scripts.

## Environment

- Language: Python
- Core libraries: OpenCV (`cv2`), NumPy
- Target hardware: Jetson (CUDA, GStreamer integration is the end goal)

## Learning curriculum

Topics are ordered by dependency. Do not skip ahead.

### Phase 1 — Foundations

| # | Topic | Key concepts | Key functions |
|---|-------|-------------|---------------|
| 1 | NumPy & image arrays | shape, dtype (uint8/float32), indexing, slicing, copy vs view | `array.shape`, `np.zeros`, `np.copy` |
| 2 | Read / display / save | file I/O, BGR vs RGB vs grayscale | `cv2.imread`, `cv2.imshow`, `cv2.imwrite`, `cv2.waitKey` |
| 3 | Coordinates & ROI | pixel addressing `[y, x]` not `[x, y]`, crop, modify pixels | slicing `image[y1:y2, x1:x2]` |
| 4 | Color spaces | BGR → GRAY, BGR → HSV, LAB, YUV | `cv2.cvtColor` |
| 5 | Basic image operations | resize, rotate, flip, translate, brightness, contrast | `cv2.resize`, `cv2.flip`, `cv2.rotate`, `cv2.convertScaleAbs` |
| 6 | Drawing & annotation | lines, rectangles, circles, text, bounding boxes | `cv2.line`, `cv2.rectangle`, `cv2.circle`, `cv2.putText` |

### Phase 2 — Image processing

| # | Topic | Key concepts | Key functions |
|---|-------|-------------|---------------|
| 7 | Thresholding & masks | binary, adaptive, Otsu, `inRange` | `cv2.threshold`, `cv2.adaptiveThreshold`, `cv2.inRange` |
| 8 | Filtering & smoothing | blur, Gaussian, median, bilateral | `cv2.blur`, `cv2.GaussianBlur`, `cv2.medianBlur`, `cv2.bilateralFilter` |
| 9 | Edge detection | Sobel, Laplacian, Canny, gradients | `cv2.Sobel`, `cv2.Laplacian`, `cv2.Canny` |
| 10 | Morphological ops | erosion, dilation, opening, closing, gradient | `cv2.erode`, `cv2.dilate`, `cv2.morphologyEx` |
| 11 | Contours & shapes | find/draw contours, area, perimeter, bounding rect, moments, centroid | `cv2.findContours`, `cv2.drawContours`, `cv2.contourArea`, `cv2.boundingRect`, `cv2.moments` |
| 12 | Histograms | brightness distribution, equalization, CLAHE | `cv2.calcHist`, `cv2.equalizeHist`, `cv2.createCLAHE` |

### Phase 3 — Geometry & features

| # | Topic | Key concepts | Key functions |
|---|-------|-------------|---------------|
| 13 | Geometric transforms | affine, perspective, homography, warping | `cv2.warpAffine`, `cv2.warpPerspective`, `cv2.getPerspectiveTransform` |
| 14 | Feature detection | keypoints, descriptors, ORB, SIFT, matching | `cv2.ORB_create`, `cv2.SIFT_create`, `cv2.BFMatcher`, `cv2.FlannBasedMatcher` |
| 15 | Camera calibration | intrinsic matrix, distortion, undistortion | `cv2.calibrateCamera`, `cv2.undistort` |

### Phase 4 — Video & motion

| # | Topic | Key concepts | Key functions |
|---|-------|-------------|---------------|
| 16 | Video basics | frame loop, FPS, latency, VideoCapture/Writer | `cv2.VideoCapture`, `cv2.VideoWriter` |
| 17 | Object tracking | frame differencing, background subtraction, optical flow, Kalman | `cv2.createBackgroundSubtractorMOG2`, `cv2.calcOpticalFlowPyrLK`, `cv2.TrackerCSRT_create` |

### Phase 5 — Detection & AI bridge

| # | Topic | Key concepts | Key functions |
|---|-------|-------------|---------------|
| 18 | Classical detection | template matching, Hough lines/circles, cascades, color detection | `cv2.matchTemplate`, `cv2.HoughLines`, `cv2.HoughCircles`, `cv2.CascadeClassifier` |
| 19 | OpenCV DNN | load models, blob preprocessing, inference, NMS | `cv2.dnn.readNet`, `cv2.dnn.blobFromImage`, `cv2.dnn.NMSBoxes` |

### Phase 6 — Performance & Jetson

| # | Topic | Key concepts |
|---|-------|-------------|
| 20 | Performance optimization | avoid copies, ROI over full image, profiling, `cv2.getTickCount` |
| 21 | OpenCV with CUDA | GpuMat, upload/download cost, full GPU pipelines |
| 22 | GStreamer integration | appsink/appsrc, pixel formats, BGR/NV12, timestamps, queues |

## Beginner project sequence

| # | Project | Concepts practiced |
|---|---------|-------------------|
| 1 | Load image and crop a region | imread, ROI slicing |
| 2 | Convert to grayscale and HSV | cvtColor |
| 3 | Detect a color using HSV mask | inRange, bitwise ops |
| 4 | Detect edges with Canny | GaussianBlur → Canny |
| 5 | Detect simple objects using contours | threshold → findContours |
| 6 | Draw bounding boxes around detected objects | boundingRect, rectangle |
| 7 | Measure object area or center point | contourArea, moments |
| 8 | Correct perspective of a rectangular object | getPerspectiveTransform, warpPerspective |
| 9 | Process all images in a folder | os/glob, batch loop |
| 10 | Apply same algorithm to video frames | VideoCapture frame loop |
| 11 | Replace video with GStreamer camera input | GStreamer pipeline string |
| 12 | Send processed frames back to GStreamer | appsrc |

## Progress tracking

Track completed topics and scripts here as the project grows.

### Completed topics
- Topic 1 — NumPy & image arrays
- Topic 2 — Read / display / save
- Topic 3 — Coordinates & ROI
- Topic 4 — Color spaces
- Topic 5 — Basic image operations
- Topic 6 — Drawing & annotation
- Topic 7 — Thresholding & masks
- Topic 8 — Filtering & smoothing
- Topic 9 — Edge detection
- Topic 10 — Morphological ops
- Topic 11 — Contours & shapes
- Topic 12 — Histograms
- Topic 13 — Geometric transforms (skipped for now)
- Topic 15 — Camera calibration (skipped for now)

### Completed projects
- None yet

### Scripts

| File | Topic | Description |
|------|-------|-------------|
| `01_numpy_basics.ipynb` | Topic 1 — NumPy & image arrays | Array creation, dtype, indexing, slicing, copy vs view, masking, basic math, drawing with NumPy |
| `02_read_write_display.ipynb` | Topic 2 — Read / display / save | imread, imwrite (jpg/png/bmp), IMREAD_GRAYSCALE, cvtColor, channel swap, resize, crop, convertScaleAbs |
| `03_roi_and_coordinates.ipynb` | Topics 3 & 6 — Coordinates/ROI & Drawing | Pixel modification, ROI extraction, region copy/paste, rectangle, circle, line, putText |
| `04_color_spaces.ipynb` | Topic 4 — Color spaces | BGR/RGB/GRAY/HSV conversions, cv2.split, inRange color detection, bitwise_and masking, contours preview |
| `05_basic_image_operations.ipynb` | Topic 5 — Basic image operations | resize, rotate, flip, translate, brightness, contrast, warpAffine, getRotationMatrix2D, convertScaleAbs |
| `06_thresholds_and_masking.ipynb` | Topic 7 — Thresholding & masks | binary/inverted threshold, NumPy vs cv2 comparison, adaptive (Gaussian), Otsu, blur+threshold pipeline, bitwise_and masking |
| `07_filtering_and_smoothing.ipynb` | Topic 8 — Filtering & smoothing | mean blur, Gaussian blur, median blur, bilateral filter |
| `08_edge_detection.ipynb` | Topic 9 — Edge detection | Sobel, Laplacian, Canny, blur+Canny pipeline, ipywidgets interactive tuner, edge overlay |
| `09_morphological_ops.ipynb` | Topic 10 — Morphological ops | erosion, dilation, opening, closing, kernel shapes (rect, ellipse, cross) |
| `10_contours_shape_analysis.ipynb` | Topic 11 — Contours & shapes | findContours, drawContours, area, perimeter, boundingRect, moments, centroid, filter by area |
| `11_histograms.ipynb` | Topic 12 — Histograms | brightness distribution, equalization, CLAHE, color histograms, ROI histograms, LAB color CLAHE |

## Key reminders

- OpenCV uses **BGR** by default, not RGB. Convert explicitly before using matplotlib or passing to AI models.
- Pixels are addressed as `image[y, x]`, not `image[x, y]`.
- Filtering (blur) almost always comes **before** edge detection or thresholding.
- Classic pipeline: `image → grayscale → threshold → morphology → contours → bounding boxes`
- On Jetson: GPU acceleration only pays off when processing savings exceed the CPU↔GPU transfer cost.
