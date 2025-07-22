# RGB Color Detection

## Overview

This project captures video from webcam and determines the dominant color (Red, Green, or Blue) by calculating the mean values of each RGB channel and comparing them.

<img src="https://github.com/user-attachments/assets/959198ff-eaa0-4618-853a-5e25167658e0" width="500"/>

**Improved Version (`detect_rgb_improve.py`)**: Enhanced color detection using HSV color space with ROI (Region of Interest) analysis. Detects 9+ colors including red, orange, yellow, green, cyan, blue, purple, pink, white, black, and gray with better accuracy.

<img width="500" src="https://github.com/user-attachments/assets/ec3454ee-f7df-4749-8f4a-6b64fe3c16bc" />

## Technologies

- **OpenCV**: Video capture and image processing
- **NumPy**: Mathematical operations and array handling

## Usage

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the basic version:
```bash
python detect_rgb.py
```

3. Run the improved version:
```bash
python detect_rgb_improve.py
```