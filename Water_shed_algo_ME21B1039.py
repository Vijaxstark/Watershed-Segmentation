#ME21B1039
#Vijay Krishna RV
#Assignment 3

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('water_coins.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Step 1 :  original image
plt.figure()
plt.title('Original Image')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.axis('off')

# Step 2 : Grayscale image
plt.figure()
plt.title('Gray Image')
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

# Step 3:  Binary image
_, thresh = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
plt.figure()
plt.title('Binary Image')
plt.imshow(thresh, cmap='gray')
plt.axis('off')

# Step 4: Erosion + Dilation
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=3)
plt.figure()
plt.title('Image after Opening (Erosion + Dilation)')
plt.imshow(opening, cmap='gray')
plt.axis('off')

#Step 5 : Sure background
sure_bg = cv.dilate(opening, kernel, iterations=3)
plt.figure()
plt.title('Sure Background')
plt.imshow(sure_bg, cmap='gray')
plt.axis('off')

#Step 6: Sure foreground
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
_, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
plt.figure()
plt.title('Sure Foreground')
plt.imshow(sure_fg, cmap='gray')
plt.axis('off')

# Step 7 :Unknown regions
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
plt.figure()
plt.title('Unknown Region')
plt.imshow(unknown, cmap='gray')
plt.axis('off')

# STEP 8 :Labelling
_, markers = cv.connectedComponents(sure_fg)
markers += 1
markers[unknown == 255] = 0

# Apply the watershed algorithm
markers = cv.watershed(img, markers)

img[markers == -1] = [255, 0, 0]  #marking borders with red
unique_markers = np.unique(markers)

# Assign random colors to each segment
segmented_img = np.zeros_like(img)
for marker in unique_markers:
    if marker == -1:  # dont diclude boundary marker
        continue
    color = np.random.randint(0, 255, size=(3), dtype=np.uint8)
    segmented_img[markers == marker] = color

# Final segmented image
plt.figure()
plt.title('Final Segmented Image with Random Colors')
plt.imshow(cv.cvtColor(segmented_img, cv.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
