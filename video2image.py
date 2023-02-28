

import cv2 

# Opens the Video file 
vidObj = cv2.VideoCapture("video.mp4") 
count = 0
success = 1
  
while success: 
    # vidObj object calls read 
    # function extract frames 
    success, image = vidObj.read() 

    # Saves the frames with frame-count 
    cv2.imwrite("frame%d.jpg" % count, image) 

    count += 1