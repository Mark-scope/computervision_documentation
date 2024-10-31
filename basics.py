import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # this method is used to detect edges in an image
cv.imshow('Canny Edges', canny)

# Dilating the image
dilaled = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilaled)

# Eroding , this method is used to erode the image that is dilated
eroded = cv.erode(dilaled, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

k = cv.waitKey(0)