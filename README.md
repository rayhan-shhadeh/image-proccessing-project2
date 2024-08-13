# Gamma Correction using OpenCV

This project demonstrates gamma correction on a grayscale image using two methods: Look-Up Table (LUT) and pixel-wise modification. The code compares the performance of both methods in terms of execution time and visualizes the results through histograms.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction

Gamma correction is a technique used to adjust the brightness of an image by applying a non-linear transformation to the pixel values. This project performs gamma correction on a grayscale image using two methods:
1. **Look-Up Table (LUT) Method**: This method precomputes the gamma correction values for all possible pixel values and stores them in a LUT, which is then used to transform the image.
2. **Pixel-wise Modification Method**: This method directly applies the gamma correction formula to each pixel individually.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/gamma-correction-opencv.git
    cd gamma-correction-opencv
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python-headless numpy matplotlib
    ```

## Usage

1. Place your image file in the project directory and update the image file name in the code if necessary:
    ```python
    img = cv.imread('your-image.jpg')
    ```

2. Run the script:
    ```sh
    python gamma_correction.py
    ```

3. The script will display the original image, grayscale image, and gamma-corrected images using both methods. It will also plot the histograms before and after processing and print the execution times for both methods.

## Results

The script outputs the following:

1. **Images**:
    - Original Image
    - Grayscale Image
    - Gamma Corrected Image using LUT
    - Gamma Corrected Image using Pixel-wise Modification

2. **Histograms**:
    - Histogram before processing
    - Histogram after processing using LUT
    - Histogram after processing using Pixel-wise Modification

3. **Execution Time**:
    - Execution time using LUT method
    - Execution time using pixel-wise modification method

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
