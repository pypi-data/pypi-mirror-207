Examples
=======================

## Quick Start Example:
<br>

Users can get more images by passing their pre-existing grayscale images using image augmentation techniques.
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

<br>

## Image Augmentation: Rotation
This use case is only for rototating the image clockwise by 90 degrees.
```python
import Augmentum
#replace image by the actual grayscale image values
image =  [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
#or instead upload a .raw image file under '.../Augmentum/Augmentum/data/'and
#call process_image() to get a list of lists representations of your grayscale image however
#you have to specify the number of ROWS and COLS in your image (default value is 512x512)
image = Augmentum.process_image(ROWS=512, COLS=512)
new_image = Augmentum.rotate(image)
```
<br>

## Image Augmentation: Reflection
This use case is only for reflecting the image by its central vertical axis.
```python
import Augmentum
#replace image by the actual grayscale image values
image =  [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
#or instead upload a .raw image file under '.../Augmentum/Augmentum/data/'and
#call process_image() to get a list of lists representations of your grayscale image however
#you have to specify the number of ROWS and COLS in your image (default value is 512x512)
image = Augmentum.process_image(ROWS=512, COLS=512)
new_image = Augmentum.reflect(image)
```
<br>


## Image Augmentation: Reflection
This use case is only for shifting the image to the right by x units.
```python
import Augmentum
#replace this by how much you want to shift the image to the right
x = 5
#replace image by the actual grayscale image values
image =  [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
#or instead upload a .raw image file under '.../Augmentum/Augmentum/data/'and
#call process_image() to get a list of lists representations of your grayscale image however
#you have to specify the number of ROWS and COLS in your image (default value is 512x512)
image = Augmentum.process_image(ROWS=512, COLS=512)
new_image = Augmentum.right_shift(image, x)
```
<br>

## Image Augmentation: Upsample Scaling
This use case is only for scaling the size of the image by a factor of 2 by upsampling.
```python
import Augmentum
#replace image by the actual grayscale image values
image =  [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
#or instead upload a .raw image file under '.../Augmentum/Augmentum/data/'and
#call process_image() to get a list of lists representations of your grayscale image however
#you have to specify the number of ROWS and COLS in your image (default value is 512x512)
image = Augmentum.process_image(ROWS=512, COLS=512)
new_image = Augmentum.upsample_scaling(image)
```
