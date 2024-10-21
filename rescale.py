import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.2):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # this works only with live video
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()  # this method is used to read the video frame by frame
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)  # this method is used to display the video frame in a new window
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()  # this method is used to release the video capturer
cv.destroyAllWindows()  # this method is used to destroy all the windows

