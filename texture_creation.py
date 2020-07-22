# Import the relevant modules
import cv2 as cv
import numpy as np
from colorthief import ColorThief

# get the texture of the flame
color_thief = ColorThief('imgHQ00096.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)

# get the smpl mask
segm_with_short = cv.imread('blend.png')


#This is for the male
for h in range(height):
    for w in range(width):
        if np.array_equal(segm_with_short[w][h], [255,255,255]):
            continue
        else:
            #since opencv uses BGR
            segm_with_short[w][h] = dominant_color[::-1]

cv.imwrite('test.png', segm_with_short)
