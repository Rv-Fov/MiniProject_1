import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

if not os.path.exists('Tahap'):
    os.makedirs('Tahap')

img = cv2.imread('parking_ori.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Tahap/1_grayscale.png', gray) 

# Blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imwrite('Tahap/2_blur.png', blur)

# Thresholding Otsu
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('Tahap/3_threshold.png', thresh)

# MORPHOLOGY
kernel_close = np.ones((15, 15), np.uint8)
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_close)

kernel_open = np.ones((5, 5), np.uint8)
opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel_open)
cv2.imwrite('Tahap/4_morphology.png', opened)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(opened, connectivity=8)

result_img = img_rgb.copy()
car_count = 0

for i in range(1, num_labels):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    
    aspect_ratio = float(w) / h
    
    if area > 3500 and 0.6 < aspect_ratio < 2.5 and w > 40 and h > 40:
        car_count += 1
        cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 0), 3)

titles = ['1. Original', '2. Grayscale', '3. Otsu Threshold', '4. Morphology', '5. Final Result']
images = [img_rgb, gray, thresh, opened, result_img]

plt.figure(figsize=(25, 10))
for i in range(5):
    plt.subplot(1, 5, i+1)

    if i in [1, 2, 3]:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])
    plt.title(titles[i], fontsize=14, fontweight='bold')
    plt.axis('off')

plt.tight_layout()
plt.show()

