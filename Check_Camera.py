import numpy as np 
import cv2 

print("If you want to Open the Webcam Choose 0")

Option = int(input())

if(Option == 0):
    cap = cv2.VideoCapture(Option) 
    while(cap.isOpened()): 
      
        while True: 
          
            ret, img = cap.read() 
            cv2.imshow('img', img) 
            if cv2.waitKey(30) & 0xff == ord('q'): 
                    break
              
        cap.release() 
        cv2.destroyAllWindows() 
    else: 
        print("Alert ! Camera disconnected") 

else:
    print("You have choosen not to open your Webcam. Thus our project will not work")