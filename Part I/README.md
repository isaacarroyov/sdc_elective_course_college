# Part I: Road recognition (*Where am I heading?*) 🛣

## Topics

### L01: Basics of image manipulation

**OpenCV** is a free library developed by Intel. It saw the light of day in 1999. Initially made in C/C++: is a cross-platform library, can run on different operating systems (Linux, Windows, Mac OS X, Android and iOS) and can be used in many programming languages such as Java, Objective C, C# and **Python**.

It is perhaps the most important and most widely used computer vision library. It's used by everyone (universities, companies, etc.) and gives free rein to the imagination as it is free software.

In this notebook, we started with image processing in Python using this library; specifically, we will see how to load or read an image, conversion to black and white, filters, and other useful operations in the course.

### L02: Region of interest and direction algorithm

In this lesson, we applied **OpenCV** functions to perform the reading of a video and select and display the region of interest of a road. Finally, we'll show the steering algorithm.

## Finals results

At the end of this first part, we'll be able to display three different videos:

- The original video
- The binarized video (with a region of interest)
- The aerial view (with de direction algorithm)

![final_result_1](figures/final_result_1.gif)
![final_result_1](figures/final_result_2.gif)

## Required libraries

- **OpenCV** `pip install opencv-python` or `conda install opencv-python`
- **NumPy** `pip install numpy` or `conda install numpy`
- **Matplotlib** `pip install matplotlib` or `conda install matplotlib`
