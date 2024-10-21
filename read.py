import cv2 as cv


#Reading Images
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow ('Cat', img) #this method is used to display the image in a new window
# cv.waitKey(0) #this method is used to wait for a key to be pressed before closing the window



#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()#this method is used to read the video frame by frame
    cv.imshow('Video', frame) #this method is used to display the video frame in a new window

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release() #this method is used to release the video capturer
cv.destroyAllWindows() #this method is used to destroy all the windows

