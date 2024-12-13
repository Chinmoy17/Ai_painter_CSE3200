# Virtual Painter and Hand Tracking using Mediapipe

This repository contains a Python-based project that uses Mediapipe for hand tracking and OpenCV for virtual painting. Users can interact with the system using hand gestures to draw on a virtual canvas, select colors, and adjust brush thickness.

---

## Features

- Real-time hand tracking using Mediapipe.
- Virtual painting with customizable brush colors and thickness.
- Gesture-based interaction for selecting tools and colors.
- Supports saving the canvas as an image.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Mediapipe
- OpenCV
- Numpy

Install the required Python packages using:
```bash
pip install -r requirements.txt
```

---

## Project Structure

```
.
├── HandTrackingMin.py       # Basic hand tracking example
├── HandTrackingModule.py    # Hand tracking helper class
├── VirtualPainter.py        # Main application file
├── Header                   # Folder containing color selection images
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

## Usage

### 1. Run the Virtual Painter
To start the virtual painter application, run the following command:
```bash
python VirtualPainter.py
```

### 2. Hand Gestures
- **Index Finger Only**: Draw on the canvas.
- **Two Fingers (Index + Middle)**: Select tools or colors from the header.

### 3. Save the Canvas
Press a predefined key (e.g., `s`) to save the canvas as an image.

---

## Demonstration

Here is a quick demo of the Virtual Painter application:

![Demo](https://via.placeholder.com/800x400.png?text=Demo+Image+Here)

---

## Contributions

Contributions are welcome! Feel free to submit a pull request or raise an issue if you find a bug or want to improve the project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Mediapipe](https://mediapipe.dev/) for their powerful hand tracking library.
- [OpenCV](https://opencv.org/) for computer vision tools.
- [Python](https://python.org/) for making development easier and faster.

