# Augmentum
A library for doing image augmentation

[![license badge - Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-brightgreen)](./LICENSE)
![image](https://img.shields.io/github/issues/kurttepelikerim/Augmentum)
[![codecov](https://codecov.io/gh/kurttepelikerim/Augmentum/branch/main/graph/badge.svg)](https://codecov.io/gh/kurttepelikerim/Augmentum)
[![Build Status](https://github.com/kurttepelikerim/Augmentum/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/kurttepelikerim/Augmentum/actions?query=workflow%3A%22Build+Status%22)
[![PyPI](https://img.shields.io/pypi/v/Augmentum)](https://pypi.org/project/Augmentum/)
[![Docs](https://img.shields.io/badge/docs-passing-success)](https://kurttepelikerim.github.io/Augmentum/)

## Overview:
Image data augmentation is the process of generating new transformed versions of images from the given image dataset to artificially expand the dataset. Augmentum is a library for doing image data augmentation given some images. The main purpose for this library is to apply many data augmentations and allow this via a simple interface without relying on special libraries like opencv, matplotlib, pillow etc.

### Development and Contributions:
For development details and contribution instructions, please refer to the [contribution guidelines](https://github.com/kurttepelikerim/Augmentum/blob/main/CONTRIBUTING.md).

## Installation: 
First, install Python 3.7 (or later) and numpy, and then install this repo as a Python package. 

```bash
$ pip install numpy
$ pip install Augmentum
```

## Quick Start Example:
Users can get more images by passing their pre-existing images using image augmentation techniques.
```python
import Augmentum
#replace image by the actual grayscale image values
image =  [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
#or instead upload a .raw image file under '.../Augmentum/Augmentum/data/'and
#call process_image() to get a list of lists representations of your grayscale image however
#you have to specify the number of ROWS and COLS in your image (default value is 512x512)
image = Augmentum.process_image(ROWS=512, COLS=512)
new_images = Augmentum.augment_image(image)
```

