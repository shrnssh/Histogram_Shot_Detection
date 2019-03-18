import os
import cv2 
  
# Function to extract frames 
def FrameCapture(path, path_2_frames): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1


    path_frames= path_2_frames

    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite(os.path.join(path_frames, "frame%d.jpg" % count), image) 
  
        count += 1
  
# Driver Code 
#if __name__ == '__main__': 
    #FrameCapture("/home/sharan/recap_videos/recap_2/video/mp4/recap_2.mp4", "/home/sharan/recap_videos/recap_2/frames")
  
    # Calling the function 



