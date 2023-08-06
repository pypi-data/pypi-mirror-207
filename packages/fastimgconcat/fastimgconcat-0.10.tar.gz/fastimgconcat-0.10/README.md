# Concatenates a list of pictures (numpy arrays) without allocating new memory

## pip install fastimgconcat

#### Tested against Windows 10 / Python 3.10 / Anaconda


```python
from fastimgconcat import temparrays,fastconcat_horizontal,fastconcat_vertical
import numpy as np
import random
import cv2

# This code demonstrates the usage of the fastconcat_vertical()
# function to concatenate pictures (numpy arrays)
# vertically in a
# faster and more efficient way. 
# The fastconcat_vertical() function takes a list of numpy arrays and concatenates
# them vertically without allocating new memory. It is recommended to use this 
# function when you are #concatenating several pictures multiple times, and 
# the shape of the output array never (or rarely) # changes, e.g. streaming
# screenshots of 2 monitors.

# Initialize the height, width and RGB values for the numpy arrays.
height = 200
width = 500
rgbValues0 = np.zeros((height, width, 3), dtype=np.uint8)
rgbValues0[:] = [255, 0, 0]
rgbValues1 = np.zeros((height, width, 3), dtype=np.uint8)
rgbValues1[:] = [0, 0, 255]

# In the for loop, the fastconcat_vertical() 
# function is used to concatenate the numpy arrays vertically.
# If you want to concatenate them horizontally, 
# use fastconcat_horizontal() instead.

checkarraysize = True
for r in range(1000):
    fastconcat_vertical(
        [
            random.choice([rgbValues0, rgbValues1]),
            random.choice([rgbValues0, rgbValues1]),
        ],
        checkarraysize=checkarraysize,
    )
    checkarraysize = False  # If you check the array size each time, it is about 10% slower.

    # The values in temparrays.vertical / temparrays.horizontal 
    # will be changed the next iteration. Therefore,
    # it is recommended to process the output data right
    # after each iteration. If you still need the arrays,
    # copy them (e.g. temparrays.horizontal.copy()), but keep in mind that copying is expensive.

    # This code displays the concatenated image in the cv2 window "test".
    # If the 'q' key is pressed, the program breaks out of the loop and closes the window.
    cv2.imshow("test", temparrays.vertical)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()


```