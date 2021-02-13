# Section I: Road recognition (_Where am I heading?_) 🛣

## Topics
### L01: Basics of image manipulation
**`OpenCV`** is a free library developed by Intel. It saw the light of day in 1999. Originally made in C/C++: is a cross-platform library, can run on different operating systems (Linux, Windows, Mac OS X, Android and iOS) and can be used in many programming languages such as Java, Objective C, C# and **Python**.

It is perhaps the most important and most widely used computer vision library. It's used by everyone (universities, companies, etc) and gives free rein to the imagination as it is free software.

In this notebook we started with image processing in Python using this library, more specifically we will see how to load or read an image, conversion to black and white, filters and other operations that were useful in the course.

### L02: Region of interest and direction algorithm
In this lesson we applied **`OpenCV`** functions to perform the reading of a video, as well as selecting and displaying the region of interest of a road. Finally, the steering algorithm will be shown.

## Final results
At the end of this first part we'll be able to display 3 different videos:
* The original video
* The binarized video (with a region of interest)
* The aerial view (with de direction algorithm)

![final_result_1](figures/final_result_1.gif)
![final_result_1](figures/final_result_2.gif)


## Required libraries
For this notebooks we need to have the following libraries installed:
* [NumPy](https://numpy.org/install/)
* [Matplotlib](https://matplotlib.org/users/installing.html)
* [OpenCV - Windows](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)
* OpenCV - miniconda or Anaconda: `conda install opencv`
