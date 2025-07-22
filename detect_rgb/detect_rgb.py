import cv2
import numpy as np
import matplotlib.pyplot as plt

# get video
vid = cv2.VideoCapture(0)

#loop
while True:
    ret, frame = vid.read()
    
    b = frame[:,:,0] # blue channel
    g = frame[:,:,1] # green channel
    r = frame[:,:,2] # red channel
    
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
    
    if b_mean > g_mean and b_mean > r_mean:
        print("blue")
    elif g_mean > b_mean and g_mean > r_mean:
        print("green")
    else:
        print("red")
    
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()