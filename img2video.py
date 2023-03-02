

import cv2 
import os 
  
# Function to convert 
# image to video 
def convert_frames_to_video(pathIn, pathOut, fps): 
    frame_array = [] 
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))] 
  
    # for sorting the file names properly 
    files.sort(key = lambda x: int(x[5:-4])) 
  
    for i in range(len(files)): 
        filename=pathIn + files[i] 
        # reading each files 
        img = cv2.imread(filename) 
        height, width, layers = img.shape 
        size = (width,height) 

        # inserting the frames into an image array 

        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):

        # writing to a image array

        out.write(frame_array[i])

    out.release()
    
    
#write a code for cocnating two images

# Read the images to be merged 
img1 = cv2.imread('image1.jpg') 
img2 = cv2.imread('image2.jpg') 
  
# Merge the images into a single image 
merged_image = cv2.hconcat([img1, img2]) 
  
# Display the merged image to the screen 
cv2.imshow('Merged Image', merged_image)