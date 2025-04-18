# 💧 Watershed Segmentation - Coin Detection

This project implements the **Watershed Algorithm** using OpenCV to segment overlapping coins in an image. It demonstrates an end-to-end pipeline of image preprocessing, morphological operations, distance transform, and watershed-based instance segmentation.

## 📂 Files

- `Watershed_Coin_Segmentation.py`: Full pipeline for segmenting coins using watershed algorithm
- `water_coins.jpg`: Input image of overlapping coins
- `requirements.txt`: Dependencies to run the script

## 🧠 Overview

The watershed algorithm treats grayscale images as topographic surfaces, where light pixels represent peaks and dark pixels represent valleys. The idea is to "flood" the valleys starting from identified markers until they meet, forming segmentation lines.

## 🪜 Steps Implemented

1. Load and convert the image to grayscale
2. Apply Otsu's thresholding
3. Perform morphological operations (erosion, dilation)
4. Compute sure background and foreground
5. Identify unknown regions
6. Label components and apply the **watershed algorithm**
7. Visualize final segmented output with random colors

## 🔧 How to Run

Make sure you have Python and OpenCV installed:

```bash
pip install -r requirements.txt
python Watershed_Coin_Segmentation.py
```

> Replace `water_coins.jpg` with any image for custom testing.

## 🖼️ Output

The script will visualize:
- Original image
- Binary and intermediate masks
- Segmentation map with unique color overlays

## 📚 References

- [Watershed Algorithm - OpenCV Docs](https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html)
- [Distance Transform and Marker-based Segmentation](https://learnopencv.com/)

---
