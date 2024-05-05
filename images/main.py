import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
# ______________________________________________________________________________________________
img = cv.imread('nnu.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ________________________________________________________________________________________________
hist_before = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histogram before processing")
plt.xlabel("Intesity")
plt.ylabel("count of pixels")
plt.xlim([0, 256])
plt.plot(hist_before)

gamma = np.random.uniform(.1, 1)

# LUT method
LUT = np.array([((i / 255.0)**(gamma)) *
               255 for i in range(256)]).astype("uint8")
# Apply Look-up Table on Gray Image
gamma_corrected_img_lut = cv.LUT(gray, LUT)

# Method 2: Modifying Pixels Individually
# Apply Gamma Correction on Each Pixel
gamma_corrected_img_pi = np.zeros(gray.shape, dtype=np.uint8)
for i in range(gamma_corrected_img_pi.shape[0]):
    for j in range(gamma_corrected_img_pi.shape[1]):
        gamma_corrected_img_pi[i, j] = (
            (gray[i, j] / 255.0)**(gamma)) * 255

# Display Images and the Histogram before processing
cv.imshow('Original Image', img)
cv.imshow('Grayscale Image', gray)
plt.show()
# Display Images After Modification
cv.imshow('Gamma Corrected Image using LUT', gamma_corrected_img_lut)
cv.imshow('Gamma Corrected Image without LUT', gamma_corrected_img_pi)


LUT_histogram_after_processing = cv.calcHist(
    [gamma_corrected_img_lut], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histogram after processing using LUT")
plt.xlabel("Intesity")
plt.ylabel("count of pixels")
plt.xlim([0, 256])
plt.plot(LUT_histogram_after_processing)
plt.show()
# _______________________________________________________________________________________
PIX_histogram_after_processing = cv.calcHist(
    [gamma_corrected_img_pi], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogram after processing WITHOUT using LUT")
plt.xlabel("Intesity")
plt.ylabel("count of pixels")
plt.xlim([0, 256])
plt.plot(PIX_histogram_after_processing)
plt.show()
# _________________________________________________________________________________________________________________
# Compare Execution Time of Both Methods
LUT_start = time.time()
cv.LUT(gray, LUT)
LUT_end = time.time()
print("Execution Time using LUT: ", LUT_end - LUT_start)

start_time = time.time()
for i in range(gamma_corrected_img_pi.shape[0]):
    for j in range(gamma_corrected_img_pi.shape[1]):
        gamma_corrected_img_pi[i, j] = (
            (gray[i, j] / 255.0) ** (1 / gamma)) * 255
end_time = time.time()
print("Execution Time using Pixels Individually: ", end_time - start_time)

cv.waitKey(0)
