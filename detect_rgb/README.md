# RGB Color Detection

Real-time dominant color detection from webcam feed using RGB channel analysis.

## Overview

This project captures video from webcam and determines the dominant color (Red, Green, or Blue) by calculating the mean values of each RGB channel and comparing them.

## Features

- Real-time video capture from webcam
- RGB channel separation and analysis
- Dominant color classification
- Live video display with color detection results

## Technologies

- **OpenCV**: Video capture and image processing
- **NumPy**: Mathematical operations and array handling
- **Matplotlib**: Visualization support (imported, ready for extensions)

## Algorithm

1. Capture frame from webcam
2. Separate RGB channels: `frame[:,:,0]` (Blue), `frame[:,:,1]` (Green), `frame[:,:,2]` (Red)
3. Calculate mean value for each channel using `np.mean()`
4. Compare means and classify dominant color
5. Display result in console and show video feed

## Requirements

```bash
pip install opencv-python numpy matplotlib
```

## Usage

```bash
python detect_rgb.py
```

**Controls:**
- Press 'q' to quit

## Expected Output

Console will continuously print the dominant color:
```
blue
green
red
blue
...
```

## Testing

Test with colored objects in front of the camera:
- Blue paper/object → Output: "blue"
- Green paper/object → Output: "green"
- Red paper/object → Output: "red"

## Improvements

- Add threshold for more accurate classification
- Implement HSV color space for better accuracy
- Add GUI interface
- Support for more color detection 