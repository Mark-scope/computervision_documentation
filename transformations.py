import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')

cv.imshow("Park", img)

# Translation
def translate(img, x , y ):
    transMat = np.float32([[1,0, x], [0,1, y]]) # the parameters of the translation matrix are (x, y)
    dimensions = (img.shape[1], img.shape[0]) # the parameters of the dimensions are (width, height)
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, -80)  #the x and y values are the amount of pixels to translate
cv.imshow("Translated", translated)



# Rotation
def rotate(image, angle, center=None):
    (height, width) = image.shape[:2]

    if center is None:
        center = (width // 2, height // 2)

    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotation_matrix, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_ROTETED = rotate(rotated, -45)
cv.imshow('Rotated_roteded', rotated_ROTETED)   



# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img,1 )  # 0 --> vertically, 1 --> horizontally, -1 --> both
cv.imshow('Flip', flip)


# Cropping
cropped = img[200:400, 300:400] #the parameters of the crop function are (height, width)
cv.imshow('Cropped', cropped)

k = cv.waitKey(0)